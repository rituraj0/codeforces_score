from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def score(request):
    r = requests.get('http://codeforces.com/api/user.info?handles=DmitriyH;Fefer_Ivan')
    return HttpResponse(r.json(),content_type='application/json');
