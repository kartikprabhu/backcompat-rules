## tests for backcompat rules to be valid

from __future__ import unicode_literals

import os
import json
import codecs

import sys

if sys.version < '3':
    text_type = unicode
else:
    text_type = str

_RULES_LOC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../backcompat-rules')

_RULES_PROPERTIES = ('properties', 'rels')

def check_type(rules, filename):
    assert 'type' in rules, "{}: 'type' does not exist".format(filename)
    assert isinstance(rules['type'], list), "{}: 'type' is not a list".format(filename)
    for value in rules['type']:
        assert isinstance(value, text_type), "{}: '{}' in 'type' is not a string".format(filename, value)

def check_props(rules, filename):

    props = [p for p in rules if p in _RULES_PROPERTIES]
    for prop in props:
        assert isinstance(rules[prop], dict), "{}: '{}' is not a dictionary object".format(filename, prop)

        for key, values in rules[prop].items():
            assert isinstance(values, list), "{}: '{} > {}' is not a list".format(filename, prop, key)
            for value in values:
                assert isinstance(value, text_type), "{}: '{}' in '{} > {}' is not a string".format(filename, value, prop, key)

def check_rules_file(filename):
    file_path = os.path.join(_RULES_LOC, filename)
    with codecs.open(file_path, 'r', 'utf-8') as f:
        rules = json.load(f)

    check_type(rules, filename)
    check_props(rules, filename)

def test_all_rules_files():

    for filename in os.listdir(_RULES_LOC):
        check_rules_file(filename)

