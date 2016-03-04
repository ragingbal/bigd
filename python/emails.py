import sys
import json


for line in sys.stdin:
	line = line.strip()
	t = json.loads(line)
	#userid, movieid, rating, unixtime = line.split('\t')
	output = []
	person_id = str(t.get('person_id'))
	vMap = map(str, t.get('emails'))
	for v in vMap:
		output.append('\t'.join([person_id,v]))
	print '\n'.join(output)