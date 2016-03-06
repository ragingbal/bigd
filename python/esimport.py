import sys
import json

from elasticsearch import Elasticsearch,helpers

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from elasticsearch_dsl import DocType, String, Date, Nested, Boolean, analyzer



class Profile(DocType):
    person_id = String()
    name = String()
    workplaces = []
    educations = []

    class Meta:
        index = 'test-profiles'


connections.create_connection(hosts=['159.100.250.246'], timeout=20)


profiles = []

# allow up to 25 connections to each node
es = Elasticsearch(["159.100.250.246"], maxsize=25)
#es.indices.create('test')


es_index = 'active_profiles'

for line in sys.stdin:
    profile = line.strip()
    t = json.loads(profile)

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
    workplaces = t.get('workplaces')
    educations = t.get('educations')
    locations = t.get('locations')
    haves = t.get('haves')

    p = Profile()
    p.person_id = person_id
    p.name = name
    p.save()

   

    print( person_id,name,first_name,last_name,username,country_code,age,email,gender,birthday,location_independent,workplaces,educations,locations,haves)

    #res = es.index(index="test-profiles", doc_type='test_profile', body=p)




