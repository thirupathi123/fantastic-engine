import json
from json_flatten import flatten

class DataLoader:
	def __init__(self, source_info):
		self.source_info = source_info
		self.type = source_info["type"]
		self.subtype = source_info["subtype"]
		self.parser_conf = source_info.get("parser_conf", {})
	
	def load_data(self):
		pass

class JSONParser(DataLoader):
	def __init__(self, source_info):
		super(JSONParser, self).__init__(source_info)
	
	def load_data(self):
		file_path = self.source_info["file_path"]
		data = []

		with open(file_path) as fp:
			json_data = json.load(fp)
			for d in json_data:
				data.append(flatten(d))
		return data




if __name__ == "__main__":
	pass