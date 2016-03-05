
import sys
import json


'''
Imports employers into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_workplaces (person_id string,school_id string,school string,school_type string,school_year string)

INSERT OVERWRITE TABLE imp_educations SELECT TRANSFORM(lines) USING 'python educations.py' AS (person_id,school_id,school,school_type) FROM u_data;

'''


for line in sys.stdin:
    try:
        line = line.strip()
        t = json.loads(line)
        output = []
        person_id = str(t.get('person_id'))
        workplaces = t.get('workplaces')
        
        if workplaces == None:
            raise ValueError('no workplaces array')
        output = []

        for workplace in workplaces:
                employer_id = workplace['id'].encode('utf8')
                employer = workplace['employer'].encode('utf8')
                location = workplace['location'].encode('utf8')

                if 'position' in workplace.keys():
                    position = workplace['position'].encode('utf8')
                else:
                    position = 'NA'
                thisLoc = '\t'.join([person_id,employer_id,employer,location,position])
                output.append(thisLoc)
        if len(output) > 0 :
            print('\n'.join(output))

    except Exception  as e:
        pass
