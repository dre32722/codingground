import http.client
import json

conn = http.client.HTTPSConnection("apip.oracleau.cloud")

headers = {
    'x-app-key': "a4652196-e427-4134-b8d7-17104ab5d314",
    'cache-control': "no-cache",
    'postman-token': "64320944-6dad-d854-fcc6-1fd2f4691d6c"
    }

conn.request("GET", "/api/medrec/physicians", headers=headers)

res = conn.getresponse()

data = res.read()
a=data.decode("utf-8")
d=json.loads(a)
print(json.dumps(d))
d=json.loads(a)
print(json.dumps(d))