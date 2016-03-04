import sys
import json


'''
Imports langauges into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_languages (person_id string,language string);
add file /vagrant/languages.py ;
INSERT OVERWRITE TABLE imp_languages SELECT TRANSFORM(lines) USING 'python languages.py' AS (person_id,language ) FROM u_data;
select * from imp_languages limit 100 ;

'''


for line in sys.stdin:
	line = line.strip()
	t = json.loads(line)


	output = []
	person_id = str(t.get('person_id'))
	vMap = map(str, t.get('languages'))
	for v in vMap:
		output.append('\t'.join([person_id,v]))
	print '\n'.join(output)

