import http.client

conn = http.client.HTTPSConnection("apip.oracleau.cloud")

payload = "{\r\n  \"Physicians\": [\r\n    {\r\n      \"FullName\": \"Jack Johnstone\",\r\n      \"MedicalSpeciality\": \"Orthopedic Surgeon\"\r\n    }\r\n  ]\r\n}"

headers = {
    'x-app-key': "a4652196-e427-4134-b8d7-17104ab5d314",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "f6ab8680-6381-69fc-92c5-f701992f2b88"
    }

conn.request("POST", "/api/medrec/physicians", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))