import requests
import json
from wsproto import Headers


class Api_req:
    with open('./test_data/testdata.json', "r") as f1:
        f2=f1.read()
        data1 = json.loads(f2)

    get_url = data1["get_url"]
    post_url = data1["post_url"]
    delete_url = data1["delete_url"]
    put_url = data1["put_url"]

    def get_req(self):
        responce = requests.get(self.get_url)
        return responce

    def post_req(self):
        jsondata = {"name": "lagnesh", "age": 29, "employ_id": 30908}
        headers = {"content-type": "application/json"}
        responce = requests.post(self.post_url, data=json.dumps(jsondata), headers=headers)
        # responce= requests.post(self.post_url, data=jsondata, headers=headers)
        return responce

    def put_req(self):
        jsondata = {"name": "bot", "age": 1, "employ_id": 7}
        responce = requests.put(self.put_url, json=jsondata)
        return responce

    def delete_req(self):
        responce = requests.delete(self.delete_url)
        return responce
