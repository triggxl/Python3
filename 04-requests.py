"""
main transfer protocol used in the web
Javascript object Notation (JSON): an object converted to string
similar to dictionary in Python
1. client prepares request
2. client sends HTTP request
3. Server recieves request and looks for data
4. Server sends back response
.get()
.post() 
basics of https requests
"""
# import module
import requests

# send request
r = requests.get(
    "https://opentdb.com/api.php?amount=5&category=13&difficulty=easy&type=multiple"
)
# get status code
print(r.status_code)
# print request
r.text
# check type
type(r.text)
# import json module
import json

# create variable to use method of json.loads to convert string to dictionary
question = json.loads(r.text)
# check type
type(r.text)
# print object in readable way (install in CLI first)
import pprint

pprint.pprint(question)
# grab specific values
question["results"][2]["category"]
