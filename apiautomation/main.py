import json
import test_requests
import jsonpath
from wsproto import Headers


def test_get_():
    app_url = "https://reqres.in/api/users?page=2"
    responce = test_requests.get(app_url)
    value = responce.status_code
    assert value == 200


def test_get_2():
    app_url = "https://reqres.in/api/users?page=2"
    responce = test_requests.get(app_url)
    print(responce.content)
    total_books = json.loads(responce.text)
    total = jsonpath.jsonpath(total_books, 'total_pages')
    assert total[0] == 2


app_url_post = "https://reqres.in/api/users"
jsondata = {"name": "lagnesh", "age": 29, "employ_id": 30908}
headers = {"content-type": "application/json"}
responce = test_requests.post(app_url_post, data=json.dumps(jsondata), headers=headers)


def test_post_1():
    # with open ('/home/lagnesh/Pictures/ss/requestjson.json',"r") as f:
    # jsondata=json.loads(f)
    rcode = responce.status_code
    print(responce.content)
    print(rcode)
    assert rcode == 201


def test_post_content():
    text = json.loads(responce.text)
    var_name = jsonpath.jsonpath(text, "name")
    assert var_name[0] == "lagnesh"


def test_delete_before():
    app_url = "https://reqres.in/api/users/2"
    response = test_requests.get(app_url)
    print(response.text)
    # responce=test_requests.delete(app_url)
    rcode = response.status_code
    assert rcode == 200


def test_delete_after():
    app_url = "https://reqres.in/api/users/2"
    responce = test_requests.delete(app_url)
    rcode = responce.status_code
    assert rcode == 204