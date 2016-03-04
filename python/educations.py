
import sys
import json


'''
Imports education into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_educations (person_id string,school_id string,school string,school_uid string,school_type string,school_year string)

INSERT OVERWRITE TABLE imp_educations SELECT TRANSFORM(lines) USING 'python educations.py' AS (person_id,school_id,school,school_uid,school_type,school_year) FROM u_data;

'''


for line in sys.stdin:
    #try:
        line = line.strip()
        t = json.loads(line)
        output = []
        person_id = str(t.get('person_id'))
        educations = t.get('educations')
        print(educations)
        output = []

        for education in educations:
            if 'school' in education.keys():
                school_id = education['id'].encode('utf8')
                school = education['school'].encode('utf8')
                #school_uid = str(education['uid'])
                school_type = education['type'].encode('utf8')
                #school_year = 'NA' if education['year'] == None else str(education['year'])
                thisLoc = '\t'.join([person_id,school_id,school,school_type])
                output.append(thisLoc)
        if len(output) >0 :
            print('\n'.join(output))

    #except Exception  as e:
        pass
