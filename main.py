########### Python 2.7 #############
import httplib, urllib, base64
from config import params

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': params['key'],
}

params = urllib.urlencode({
    # Request parameters
    'visualFeatures': 'Categories',
})

body = {"url" : "https://upload.wikimedia.org/wikipedia/commons/5/58/Sunset_2007-1.jpg"}

try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e.message)

####################################
