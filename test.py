import urllib.request
import json
import requests

def is_json(myjson):
  try:
    json_object = json.loads(myjson.read())
  except:
    return False
  return True

url="http://codeforces.com/api/user.rating?handle=rituraj";

req = requests.get(url)

js= req.json();

print( js["status"]);


print( js["result"]);

