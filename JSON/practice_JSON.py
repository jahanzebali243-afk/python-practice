import json 

dict = {
    "name" : "jahanzeb" ,
    "rollno" : "74"
}

jsonfile = json.dumps(dict)
print (jsonfile)