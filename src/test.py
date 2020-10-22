from config import *
from data_loader import load_data
from datetime import datetime
from elasticsearch import Elasticsearch
skip = 0
es = Elasticsearch()
if __name__ == "__main__":
	data = load_data(source_info)
	print(len(data))
	params = {
		"pipeline":ingest_pipeline_id
	}
	for i, doc in enumerate(data):
		print(doc)
		if i<skip:
			continue
		doc["timestamp"] = datetime.now()
		es.index(index=index_name, id=i, body=doc, params=params)
	#doc = es.get(index=index_name, id=42)
	#print(doc)	