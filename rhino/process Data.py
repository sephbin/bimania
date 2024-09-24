import requests
import json
server = "http://localhost:8000"
#server = "https://archmanucox.pythonanywhere.com"
data = requests.get("%s/bimverse/nodes-light.json/?search=FloorSlab"%(server)).json()

# print(data)

tag = "floor"
tagIndex = requests.get("{}/bimverse/modularClasses.json/?search={}".format(server,tag)).json()[0]["id"]


for d in data:
	if tag not in d["modularClassTags"]:
		print(d)
		d["modularClassTags"] = d["modularClassTags"]+[tag]
		d["data"] = json.dumps(d["data"])
		d["server"] = server
		put = requests.put("{server}/bimverse/nodes-light/{id}/".format(**d), data=d)
		print(put.status_code)
		print(put.reason)
		with open("result.html","w") as file:
			file.write(put.text)
		break