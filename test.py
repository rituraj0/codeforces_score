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

req = urllib.request.urlopen(url).read();

r = requests.get('http://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan')

js= r.json();

print( js["status"]);


"""
req = urllib.request.urlopen(url)

xyz = req.readall().decode('utf-8');

xyz is a string 
#print( req["result"] );

for node in xyz:
  print(node)
"""

#print( xyz["result"] );

#print(data);
#print ( data['statistics']['dataCount'] );
#print json[0]['title']