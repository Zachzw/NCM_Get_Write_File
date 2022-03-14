import requests
import os

# JSON Headers for NCM
url = 'https://www.cradlepointecm.com/api/v2/routers/'

headers = {
    'X-CP-API-ID': 'xxxxxxxxx',
    'X-CP-API-KEY': 'xxxxxxxxxxxxxxxxxx',
    'X-ECM-API-ID': 'xxxxxxxxxxxxxxxxxxxxx',
    'X-ECM-API-KEY': 'xxxxxxxxxxxxx',
    'Content-Type': 'application/json'
}

# Get routers
req = requests.get(url, headers=headers)
routers_resp = req.json()
print(routers_resp)

# Open File, Append routers_resp to a file called API_Output.txt and close the file

with open('API_Output.txt', 'w')as f:
        f.write((str(routers_resp)))
        f.close
print('Wrote results to API_Output.txt')
