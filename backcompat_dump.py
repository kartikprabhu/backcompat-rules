from mf2py import backcompat
import json
import codecs

def backcompat_dump(loc):

	roots = backcompat.CLASSIC_ROOT_MAP
	props = backcompat.CLASSIC_PROPERTY_MAP

	for root in roots:
		data = {'type': [roots[root]], 'properties': props[root]}
		path = loc+root+'.json'
		with codecs.open(path, 'w', 'utf-8') as out_file:
			json.dump(data, out_file, indent=4, ensure_ascii=False)
