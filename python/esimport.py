import sys
import json

from elasticsearch import Elasticsearch,helpers

profiles = []
es = Elasticsearch()
es_index = 'active_profiles'

for line in sys.stdin:
    profile = line.strip()
    profiles.append(profile)
    if len(profiles) == 1000:
        es.bulk_index(es_index, "profile", profiles, id_field="person_id")
        profiles = []
if len(profiles) > 0:
    es.bulk_index(es_index, "profile", profiles, id_field="person_id")
