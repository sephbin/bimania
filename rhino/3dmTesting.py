import rhino3dm as rh
import requests
import json


#server = "http://localhost:8000"
server = "https://archmanucox.pythonanywhere.com"
data = requests.get("%s/bimverse/nodes.json/?search=Timber Frame"%(server)).json()



for i in data[0]["geometryObjects"]:
	#print(i)
	print(dir(rh))
	#print(rh.GeometryBase.__doc__)
	print(dir(rh.GeometryBase))
	ob = rh.Brep()
	ob.Decode(i["geometry"])
	print(dir(ob))
	print(ob.ObjectType)
	print(ob.IsSolid)
	for s in ob.Surfaces:
		print(s)