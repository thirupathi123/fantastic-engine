from data_loader.load_data import JSONParser

parsers = {
	"file_json":JSONParser
}

def load_data(source):
	if source["type"] == "file" and source["subtype"] == "json":
		return parsers[source["type"]+"_"+source["subtype"]](source).load_data()

	pass

