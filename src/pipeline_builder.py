from elasticsearch.client.ingest import IngestClient
from config import *

stage_type_parser = {

	"field_mapping":field_mapping,
	"traits_extraction":traits_extraction,
	"entity_extraction":entity_extraction,
	"keyword_extraction":keyword_extraction
}

class IngestPipeline:

	def __init__(self, name, description="", processors=[]):
		super().__init__()
		self.processors = processors
		self.name = name
		self.description = description

	
	def get_pipeline(self):
		return self.processors
	
	def create(self, es):
		p = IngestClient(es)
        p.put_pipeline(id=name, body={
            'description': self.description,
            'processors': self.processors
        })
	
	def simmulate(self, es, docs, params={}):
		docs = {
			"docs":docs
		}
		p = IngestClient(es)
		simmulate_result = p.simulate(id=name, body=docs, params=params)
		return simmulate_result
	
	def delete(self, es):
		p = IngestClient(es)
		return p.delete_pipeline(id=name, params=params)





