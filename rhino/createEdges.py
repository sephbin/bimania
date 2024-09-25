import requests
import json
#server = "http://localhost:8000"
server = "https://archmanucox.pythonanywhere.com"

tag = "door"
# data = requests.get("%s/bimverse/nodes-light.json/?modularClassTags__name=wall"%(server)).json()
data = requests.get("%s/bimverse/nodes-light.json/?search=%s"%(server, tag)).json()


level = requests.get("{}/bimverse/nodes-light.json/?modularClassTags__name=level".format(server)).json()[0]
#print(level)

# print(data)


for d in data:
	print(d)
	d["server"] = server
	d["data"] = json.dumps(d["data"])
	if tag not in d["modularClassTags"]:
		d["modularClassTags"] = d["modularClassTags"]+[tag]
		put = requests.put("{server}/bimverse/nodes-light/{id}/".format(**d), data=d)
		#print(put.json())
		#with open("result.html","w") as file:
			#file.write(put.text)
	addKey = True
	for i in d["nodeObject_to"]:
		if i["name"] == "level":
			addKey = False
	if addKey:
		p =  {
        "name": "level",
        "identifier": "----",
        "enabled": True,
        "nodeObject_from": d['id'],
        "nodeObject_to": level['id']
    }
		post = requests.post("{server}/bimverse/edges/".format(**d), data=p)
		print(post)
		print(post.json())

	addKey = True
	for i in d["nodeObject_to"]:
		if i["name"] == "host":
			addKey = False
	if addKey:
		p =  {
        "name": "host",
        "identifier": "----",
        "enabled": True,
        "nodeObject_from": d['id'],
        "nodeObject_to": json.loads(d['data'])['HostID']
    }
		post = requests.post("{server}/bimverse/edges/".format(**d), data=p)
		print(post)
		print(post.json())	