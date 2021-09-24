from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan, bulk

es_client = Elasticsearch(hosts=[]) # fill it
es_query = {
    "query": {"match_all": {}}
}
es_index = 'INDEX_NAME'
docs = scan(es_client,
            query=es_query,
            index=es_index,
            scroll='1m',
            size=1000)

def create_document(hits):
    for doc in hits:
        doc.pop('_score')
        _id = doc.pop('_id')
        _source = doc.pop('_source')
        # // code here
        # //
        new_document = {
            "_op_type": "create",
            "_index": es_index,
            "_source": _source,
            "_id": _id
        }
        yield new_document
        
bulk(es_client, create_document(docs))
