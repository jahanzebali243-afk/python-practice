'''
import json 
with open ("myfile.json" , "w")as f:
my_dict = {
    "name" : "jahanzeb" ,
    "rollno" : "74"
}
json.dump( my_dict , f , indent=2) 
    '''

import json

my_dict = {
    "name": "jahanzeb",
    "rollno": "74"
}

with open("myfile.json", "w") as f:
    json.dump(my_dict, f, indent=2)
    print ("File written sucessfully")