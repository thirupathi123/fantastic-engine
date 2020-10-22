from config import *
from data_loader import load_data
from datetime import datetime
from elasticsearch import Elasticsearch
skip = 0
es = Elasticsearch()
def index_docs(source_info, index_id, pipeline_id):
	data = load_data(source_info)
	print(len(data))
	params = {
		"pipeline":pipeline_id
	}
	for i, doc in enumerate(data):
		print(doc)
		if i<skip:
			continue
		doc["timestamp"] = datetime.now()
		es.index(index=index_id, id=i, body=doc, params=params)
	#doc = es.get(index=index_name, id=42)
	#print(doc)	