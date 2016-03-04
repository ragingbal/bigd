
import sys
import json


'''
Imports education into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_educations (person_id string,school_id string,school string,school_uid string,school_type string,school_year string)

INSERT OVERWRITE TABLE imp_educations SELECT TRANSFORM(lines) USING 'python educations.py' AS (person_id,school_id,school,school_uid,school_type,school_year) FROM u_data;

'''


for line in sys.stdin:
	try:
		line = line.strip()
		t = json.loads(line)
		output = []
		person_id = str(t.get('person_id'))
		educations = t.get('educations')
		output = []
		for education in educations:
			school_id = education['id'].encode('utf8')
			school = education['school'].encode('utf8')
			school_uid = education['school_uid'].encode('utf8')
			school_type = education['type'].encode('utf8')
			school_year = education['year'].encode('utf8')
			thisLoc = '\t'.join([person_id,school_id,school,school_uid,school_type,school_year])
			output.append(thisLoc)
		print('\n'.join(output))

	except Exception  as e:
        pass
