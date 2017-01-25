import requests

url = 'https://eservices.mas.gov.sg/api/action/datastore/search.json?resource_id=110873fe-3e36-4214-8c04-c3045170796c&limit=5'

r = requests.get(url)
# json_data = r.json()

# 선언형으로 해볼까 시간걸리니까 ㅎ

json_data = r.json()

# 정확하게 파싱이 안되는듯 ㅠ 이거 좀더 연구해봐야겠네...


for k in json_data.keys():
    print(k + " : ", json_data[k])
