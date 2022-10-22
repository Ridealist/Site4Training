from elasticsearch import Elasticsearch

es = Elasticsearch()

es.indices.delete(index='test_index', ignore=[400, 404])

body = {
    "settings": {
        "index": {
            "analysis": {
                "analyzer": {
                    "korean": {
                        "tokenizer": "nori_tokenizer"
                    }
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "korean"
            },
            "description": {
                "type": "text"
            }
        }
    }
}

es.indices.create(index='test_index', body=body)

doc1 = {
    "title": "좋은 수업",
    "description": "설명 주절주절"
}

es.index(index="test_index", doc_type="_doc", body=doc1)

# resp = es.bulk()

q = {
    "size": 1,
    "query": {
        "match": {
            "title": "수업"
        }
    }
}

es.search(index="test_index", body=q)