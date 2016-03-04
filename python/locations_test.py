import sys
import json



f = open("people.json",'r')

count = 0

for line in f:
	#print(line)
	t = json.loads(line)
	output = []
	person_id = str(t.get('person_id'))

	locations = t.get('locations')
	output = []
	for location in locations:
		#thisLoc = map(str, location)
		print(location)
		source = str(location['source'].encode('utf8'))
		geocoded_name = str(location['geocoded_name'].encode('utf8'))
		lid = str(location['id'].encode('utf8'))
		location_type = str(location['location_type'].encode('utf8'))


		
		thisLoc = '\t'.join([person_id,lid,source,geocoded_name])
		output.append(thisLoc)
	print('\n'.join(output))


