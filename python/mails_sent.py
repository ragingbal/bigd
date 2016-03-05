import sys
import json


for line in sys.stdin:
    line = line.strip()
    t = json.loads(line)

    output = []
    person_id = str(t.get('person_id'))
    vMap = map(str, t.get('mails_sent'))
    for v in vMap:
        output.append('\t'.join([person_id,v]))
    if len(vMap) > 0: 
        print '\n'.join(output)