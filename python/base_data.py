#!/usr/bin/python

import sys
import json



'''
Base data of the user. 

CREATE TABLE imp_base (person_id string,name string,first_name string,last_name string,username string,country_code string,age string,email string,gender string,birthday string,location_independent string)
add file /home/hive/gm_scripts/base_data.py ;
INSERT OVERWRITE TABLE imp_base SELECT TRANSFORM(lines) USING 'python base_data.py' AS (person_id,name,first_name,last_name,username,country_code,age,email,gender,birthday,location_independent) FROM u_data;
select * from imp_base limit 100 ;


'''

#f = open("people.json",'r')
#w = open("test.out",'w+')
#for line in f:

for line in sys.stdin:
	try:
		line = line.strip()
		t = json.loads(line)
		person_id = 'NA' if t.get('person_id') == None else str(t.get('person_id'))	
		name = 'NA' if t.get('name') == None else t.get('name').encode('utf8')
		first_name = 'NA' if t.get('first_name') == None else t.get('first_name').encode('utf8')
		last_name = 'NA' if t.get('last_name') == None else t.get('last_name').encode('utf8')
		username = 'NA' if t.get('username') == None else t.get('username').encode('utf8')
		country_code = 'NA' if t.get('country_code') == None else t.get('country_code').encode('utf8')
		age = 'NA' if t.get('age') == None else str(t.get('age'))
		email = 'NA' if t.get('email') == None else t.get('email').encode('utf8')
		gender = 'NA' if t.get('gender') == None else t.get('gender').encode('utf8')
		birthday ='NA' if t.get('birthday') == None else t.get('birthday')
		location_independent ='NA' if t.get('location_independent') == None else t.get('location_independent')

		print ('\t'.join([person_id,name,first_name,last_name,username,country_code,age,email,gender,birthday,location_independent]))

	except Exception  as e:
        pass
