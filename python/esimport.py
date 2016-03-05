import sys
import json

from elasticsearch import Elasticsearch,helpers

profiles = []

# allow up to 25 connections to each node
es = Elasticsearch(["159.100.250.246"], maxsize=25)
#es.indices.create('test')


es_index = 'active_profiles'

for line in sys.stdin:
    profile = line.strip()
    res = es.index(index="test-index", doc_type='profile', body=profile)

 '''
    profiles.append(profile.decode('utf8'))
    if len(profiles) == 1000:
        helpers.bulk(es,profiles)
        profiles = []
if len(profiles) > 0:
    helpers.bulk(es,profiles)
'''