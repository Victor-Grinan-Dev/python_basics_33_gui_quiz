# API = aplication programing interface
"""interacting with external systems
    API request for information"""

import requests

iss_endpoint = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url=iss_endpoint)

# 100 - hold on
# 200 - here you go
# 300 - go permission denied
# 400 - not existing or you screw up somehow
# 500 - server problems

print(response.status_code)
# if response.raise_for_status == 404:
#     raise Exception(" Resource doesn't exits")
# elif response.status_code == 401:
#     raise Exception("data access not authorized")
response.raise_for_status() # instead of manual working the exeption
data = response.json()
print(data)
data1 = response.json()['iss_position']
data2 = response.json()['message']
data3 = response.json()['timestamp']

print(data1)
print(data2)
print(data3)

data4 = response.json()['iss_position']['longitude']
data5 = response.json()['iss_position']['latitude']

satelite_position = data4, data5

print(satelite_position)


