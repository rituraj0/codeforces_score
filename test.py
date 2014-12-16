import urllib.request
import json
import requests

def is_json(myjson):
  try:
    json_object = json.loads(myjson.read())
  except:
    return False
  return True

url0="http://codeforces.com/api/user.rating?handle=rituraj";

url="http://codeforces.com/api/user.status?handle=rituraj&from=1&count=10";


req = requests.get(url)

js= req.json();

print( js["status"]);


#print( js["result"]);


#check S-Ok , then go 

for sub in js["result"]:
   print( sub["id"])

