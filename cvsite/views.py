from django.shortcuts import render
from urllib.request import urlopen
from django.http import HttpResponse
from io import BytesIO
import json
import gzip
from cvsite.profiles import repositories, reputation

def profiles(request):
    profiles = {
        'repositories' : repositories(),
        'reputation' : reputation()
    }

    return HttpResponse(
        content = json.dumps(profiles),
        mimetype = 'application/json'
    )
