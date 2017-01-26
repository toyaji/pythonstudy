import urllib.request

url = 'https://eservices.mas.gov.sg/api/action/datastore/search.json?resource_id=110873fe-3e36-4214-8c04-c3045170796c&limit=5'

with urllib.request.urlopen(url) as req:
    print(req.read())