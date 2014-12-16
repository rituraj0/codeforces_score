from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def score(request):
    url0="http://codeforces.com/api/user.rating?handle=rituraj";
    url="http://codeforces.com/api/user.status?handle=rituraj&from=1&count=10";
    req = requests.get(url)
    js= req.json();

    dict={}

    req_time = "2014-12-16";
    total_point = 0;
    
    ans_string = req_time;

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

       ans_string = ans_string + "\n" + str(sub["problem"]["contestId"]) + "   " + str(sub["problem"]["index"]) + "   " + str(curr_point);

    print( total_point) ;

    ans_string = ans_string + "\n" + " total point is " + str(total_point);

    print( ans_string);

    r = requests.get('http://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan')
    return HttpResponse(r.json(),content_type='application/json');
