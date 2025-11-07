import os
import pprint
import requests

url = "https://api.docuseal.com/submitters"

headers = {
    #"X-Auth-Token": os.getenv("API_TOKEN")
    "X-Auth-Token" : 'FmzWAds1rshavQtaN3BWjSvnHsrW9vuUVLTBMjDuZM4'
}


response = requests.get(url, headers=headers)
data = response.json()
names = []
ChristmasPlayNames = []

#pprint.pprint(data)

if response.status_code == 200:
    for submission in data.get('data',[]):
        permissionSlipName = submission['template']['name']                             # Specify the specific permission slip
        status = submission['status']                                                   # Getting the status of the form
        values_map = {v['field'] : v['value'] for v in submission.get('values',[])}         
        cac_em_name = values_map.get('Text Field 2')

        if(permissionSlipName == "Lock-In Permission Slip" and status == "completed"):
            names.append(cac_em_name)
        elif (permissionSlipName == "Christmas Play Permission Slip" and status == "completed"):
            ChristmasPlayNames.append(cac_em_name)
else:
    print("Error: ", response.status_code)

print(names)
print(ChristmasPlayNames)
