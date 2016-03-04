#!/usr/bin/python

import sys
import json

'''
Imports emails into new table. Have skipped fields which do not always exist.

CREATE TABLE imp_emails (person_id string,email string);
add file /vagrant/emails.py ;
INSERT OVERWRITE TABLE imp_emails SELECT TRANSFORM(lines) USING 'python emails.py' AS (person_id,email ) FROM u_data;
select * from imp_languages limit 100 ;

'''

for line in sys.stdin:
    try:
        line = line.strip()
        t = json.loads(line)
        output = []
        person_id = str(t.get('person_id'))
        vMap = map(str, t.get('emails'))
        for v in vMap:
            output.append('\t'.join([person_id,v]))
        print '\n'.join(output)
    except Exception  as e:
        pass
