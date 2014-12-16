import urllib.request
import json
import requests
import datetime

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
   print( sub["id"] , sub["contestId"] , sub["creationTimeSeconds"], sub["problem"]["contestId"] ,sub["problem"]["index"])
   localseconds = sub["creationTimeSeconds"] +  19800; # convert to local IST 
   print( datetime.datetime.fromtimestamp(localseconds).strftime('%Y-%m-%d %H:%M:%S') )

# contestId
# creationTimeSeconds

# "problem" contestId":494 index