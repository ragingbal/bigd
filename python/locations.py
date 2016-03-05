
import sys
import json


'''
Imports location into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_locations (person_id string,id string, geocoded_name string,source string,location_type string)

INSERT OVERWRITE TABLE imp_locations SELECT TRANSFORM(lines) USING 'python locations.py' AS (person_id,id ,geocoded_name ,source ,location_type ) FROM u_data;

'''


for line in sys.stdin:
    try:
        line = line.strip()
        t = json.loads(line)
        output = []
        person_id = str(t.get('person_id'))
        locations = t.get('locations')
        output = []
        for location in locations:
            source = location['source'].encode('utf8')
            geocoded_name = location['geocoded_name'].encode('utf8')
            lid = str(location['id'])
            location_type = location['location_type'].encode('utf8')
            thisLoc = '\t'.join([person_id,lid,geocoded_name,source,location_type])
            output.append(thisLoc)
        print('\n'.join(output))

    except Exception  as e:
        pass
