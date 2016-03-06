import sys
import json

from elasticsearch import Elasticsearch,helpers

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from elasticsearch_dsl import DocType, String, Date, Nested, Boolean, analyzer



class ProfileNew(DocType):
    person_id = String()
    name = String()
    country_code = String()
    location_independent = String()
    gender = String()
    workplaces = []
    educations = []
    locations = []
    haves = []

    class Meta:
        index = 'new-profiles'


connections.create_connection(hosts=['159.100.250.246'], timeout=20)


profiles = []

# allow up to 25 connections to each node
es = Elasticsearch(["159.100.250.246"], maxsize=25)
#es.indices.create('test')


es_index = 'active_profiles'

skiplist = []
skiplist.append('cv')
skiplist.append('friend_ids')

for line in sys.stdin:
    profile = line.strip()
    
    t = json.loads(profile)
    for skip in skiplist:
        t.pop(skip, None)


   
    res = es.index(index="pop-profiles", doc_type='test_profile', body=t)




