import requests

data = requests.get("https://archmanucox.pythonanywhere.com/bimverse/nodes-light.json/?search=Floor Slab").json()

# print(data)

for d in data:
	if "floor" not in d["modularClassTags"]:
		# print(d)
		d["modularClassTags"] = d["modularClassTags"]+["floor"]
		requests.put("https://archmanucox.pythonanywhere.com/bimverse/nodes-light/{id}".format(**d), data=d)
		print(d)
		break