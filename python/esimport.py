import sys
import json

from elasticsearch import Elasticsearch,helpers
from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Search
from elasticsearch_dsl import DocType, String, Date, Nested, Boolean, analyzer


profiles = []

# allow up to 25 connections to each node
es = Elasticsearch(["159.100.250.246"], maxsize=25)
#es.indices.create('test')


es_index = 'active_profiles'

skiplist = []
skiplist.append('cv')
skiplist.append('friend_ids')
skiplist.append('mails_disabled')
skiplist.append('crawled_at')
skiplist.append('uninstalled')
skiplist.append('incomplete')
skiplist.append('initialized_at')
skiplist.append('logged_in_at')
skiplist.append('profile_image_url')
skiplist.append('email_settings')
skiplist.append('activated_at')
skiplist.append('test_user')
skiplist.append('black_listed')
skiplist.append('worth_indexing')
skiplist.append('needs_tour')
skiplist.append('refined')
skiplist.append('skip_tours')
skiplist.append('logins')
skiplist.append('infos')

processedCount = 0;
skippedCount = 0;


for line in sys.stdin:
    try:
        profile = line.strip()
        processedCount = processedCount + 1;
        t = json.loads(profile)
        for skip in skiplist:
            t.pop(skip, None)
        res = es.index(index="pop-profiles", doc_type='small_profile', body=t)
        print ('\t'.join(str(processedCount),str(skippedCount))

    except Exception  as e:
        skippedCount = skippedCount + 1





