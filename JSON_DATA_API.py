import base64
import requests
import json
import os

from pymongo import MongoClient

base64str = ''
url = "https://rest.resumeparsing.com/v9/parser/resume"

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'sovren-accountid': "1234567890",
    'sovren-servicekey': "abbcvaj8264efg23dwlklhsgddvbhf",
}
files = os.listdir('resume/')
print(files)
for file in files:
    with open('resume/' + file, 'rb') as f:
        print("qwertyui", f).decode('UTF-8')
        payload = {
            'DocumentAsBase64String': base64str
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        resumeJsondata = response.json()

        with open('data.json', 'a', encoding="UTF-8") as f:
            json.dump(resumeJsondata, f, ensure_ascii=False, indent=4)

        print("Parsing  done")

        client = MongoClient('mongodb://localhost:27017')
        db = client['Api-Database']
        resumeJsondataapi = db.resumeJsondata
        print(resumeJsondataapi)
        result = resumeJsondataapi.insert_one(resumeJsondata)
