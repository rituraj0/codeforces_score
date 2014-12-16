import json
import urllib.request
import requests
url='http://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan';
txt = urllib.request.urlopen(url).read()
r = requests.get('http://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan')
print( txt );