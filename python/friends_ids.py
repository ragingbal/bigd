import sys
import json


for line in sys.stdin:
	line = line.strip()
	t = json.loads(line)
	#userid, movieid, rating, unixtime = line.split('\t')

	#print '\t'.join([person_id,first_name,last_name])
	#print '\n'.join(map(str, t.get('friend_ids')))

	output = []
	person_id = str(t.get('person_id'))
	vMap = map(str, t.get('friend_ids'))
	for v in vMap:
		output.append('\t'.join([person_id,v]))
	print '\n'.join(output)

