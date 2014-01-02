from django.shortcuts import render
from urllib.request import urlopen
from io import BytesIO
import json
import gzip

def homepage(request):
    githubUser = jsonResponse('https://api.github.com/users/nottrobin')
    stackUser  = jsonResponse('http://api.stackoverflow.com/1.1/users/613540/')['users'][0]

    return render(
        request,
        'cv/index.html',
        {
            'title'       : 'Web developer',
            'repositories': githubUser['public_repos'],
            'reputation'  : stackUser['reputation']
        }
    )

def jsonResponse(url):
    response = urlopen(url)

    if response.info().get('Content-Encoding') == 'gzip':
        binaryStream = BytesIO(response.readall()  )
        zipFile = gzip.GzipFile(fileobj=binaryStream)
        responseContents = zipFile.read().decode('utf-8')
    else:
        responseContents = response.readall().decode('utf-8')

    return json.loads(responseContents)
