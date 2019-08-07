import base64
import requests #this module will need to be installed
import json
import os
from requests import async

base64str = ''
#open the file, encode the bytes to base64, then decode that to a UTF-8 string
files = os.listdir('your_directory/')
print(files)
for file in files:
    with open('resume/' + file, 'rb') as f:
        print("qwertyui",f)
        base64str = base64.b64encode(f.read()).decode('UTF-8')

url = "Request Url here....."
payload = {
    'DocumentAsBase64String': base64str
}

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'Api-account-id(if any)': "12345678",
    'api-servicekey(if any)': "OFFoOTE0QWtZQUttN2svcDRqd0tZSlgzRWV0UWY1aVBOVndySmVYdg==",
}
#make the request, NOTE: the payload must be serialized to a json string

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

async_list = []

for u in urls:
    # The "hooks = {..." part is where you define what you want to do
    #
    # Note the lack of parentheses following do_something, this is
    # because the response will be used as the first argument automatically
    action_item = async.get(u, hooks = {'response' : response})

    # Add the task to our list of things to do via async
    async_list.append(action_item)

# Do our list of things to do via async
async.map(async_list)
# this will give you the json data of the resumes
data = response.json()

with open('data.json', 'a', encoding="UTF-8") as f:
    json.dump(data,f, ensure_ascii=False, indent=4)

print("Your data is save in the data json.file")
