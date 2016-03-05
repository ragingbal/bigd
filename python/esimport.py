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