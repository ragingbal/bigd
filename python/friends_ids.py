import sys
import json


for line in sys.stdin:
    try:
        line = line.strip()
        t = json.loads(line)
        output = []
        person_id = str(t.get('person_id'))
        vMap = map(str, t.get('friend_ids'))
        for v in vMap:
            output.append('\t'.join([person_id,v]))
        if len(output) > 0:
            print '\n'.join(output)
    except Exception  as e:
        pass  