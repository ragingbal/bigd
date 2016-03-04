import sys
import json

'''
Imports logins into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_logins (person_id string,login string);
add file /vagrant/logins.py ;
INSERT OVERWRITE TABLE imp_logins SELECT TRANSFORM(lines) USING 'python logins.py' AS (person_id,login ) FROM u_data;
select * from imp_logins limit 100 ;

'''

for line in sys.stdin:
	line = line.strip()
	t = json.loads(line)

	output = []
	person_id = str(t.get('person_id'))
	vMap = map(str, t.get('logins'))
	for v in vMap:
		output.append('\t'.join([person_id,v]))
	print '\n'.join(output)

