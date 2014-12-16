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


dict={}

req_time = "2014-12-16";
total_point = 0;

for sub in reversed(js["result"]):
  
   if( (sub["problem"]["contestId"] , sub["problem"]["index"] ) in dict ):
       continue;

   localseconds = sub["creationTimeSeconds"] #+  gives right time
   
   curr_time = datetime.datetime.fromtimestamp(localseconds).strftime('%Y-%m-%d');

   if( curr_time != req_time ):
       continue;
      
   print( sub["id"] , sub["contestId"] , sub["creationTimeSeconds"], sub["problem"]["contestId"] ,sub["problem"]["index"])

   dict[ (sub["problem"]["contestId"] , sub["problem"]["index"] ) ] = True;  

   curr_point=0;

   if( sub["problem"]["index"] == "A" ):
       curr_point = 1;
   elif( sub["problem"]["index"] == "B"):
       curr_point = 2;
   elif( sub["problem"]["index"] == "C"):
       curr_point = 5;
   elif( sub["problem"]["index"] == "D"):
       curr_point = 10;
   elif( sub["problem"]["index"] == "E"):
       curr_point = 15;    

   total_point = total_point + curr_point;

print( total_point) ;

# contestId
# creationTimeSeconds

# "problem" contestId":494 index
