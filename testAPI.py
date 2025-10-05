import os
import pprint
import requests

url = "https://api.docuseal.com/submissions"

headers = {
    #"X-Auth-Token": os.getenv("API_TOKEN")
    "X-Auth-Token" : 'FmzWAds1rshavQtaN3BWjSvnHsrW9vuUVLTBMjDuZM4'
}


response = requests.get(url, headers=headers)
data = response.json()
'''
names = []
if response.status_code == 200:
    for submission in data.get('data',[]):
        values_map = {v['field'] : v['value'] for v in submission.get('values',[])}
        cac_em_name = values_map.get('Text Field 2')
        
        if cac_em_name:
            names.append(cac_em_name)
    print(names)
else:
    print("Error: ", response.status_code)

'''
pprint.pprint(data['data'][2]['status'])

