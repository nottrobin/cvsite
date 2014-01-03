from urllib.request import urlopen
from io import BytesIO
import json
import gzip

def repositories():
    return jsonResponse('https://api.github.com/users/nottrobin?client_id=4cfe6965dc7e3dadaf3f&client_secret=f1e5bf0d3fc92dc6503d1869e9e2ed10ee8a6faa')['public_repos']

def reputation():
    return jsonResponse('http://api.stackoverflow.com/1.1/users/613540/')['users'][0]['reputation']

def jsonResponse(url):
    response = urlopen(url)

    if response.info().get('Content-Encoding') == 'gzip':
        binaryStream = BytesIO(response.readall()  )
        zipFile = gzip.GzipFile(fileobj=binaryStream)
        responseContents = zipFile.read().decode('utf-8')
    else:
        responseContents = response.readall().decode('utf-8')

    return json.loads(responseContents)
