import jsonpath
import json
import pytest
from test_requests.api_reqs import Api_req
from common_utilities.loggers import Logger


logger = Logger.loggen()


rqst=Api_req()
get_response = rqst.get_req()
post_responce=rqst.post_req()
delete_responce=rqst.delete_req()
put_responce=rqst.put_req()


logger.info("First test case for get")
def test_get_1():
    value = get_response.status_code
    assert value == 200
# logger.info("First test case for get done")

logger.info("second test case for get")
def test_get_2():

    total_books = json.loads(get_response.text)
    total = jsonpath.jsonpath(total_books, 'total_pages')
    assert total[0] == 2
#failed test case


logger.info("First test case for post")
@pytest.mark.skip
def test_post_1():
    status_code=post_responce.status_code
    assert status_code==201


logger.info("Second test case for post")
def test_post_2():
    text = json.loads(post_responce.text)
    var_name = jsonpath.jsonpath(text, "name")
    assert var_name[0] == "lagnesh"
#failed test case


logger.info("First test case for delete")
@pytest.mark.skip
def test_delete_1():
    statuscode=delete_responce.status_code
    assert statuscode==204


logger.info("Second test case for delete")
def test_delete_2():
    delete_text=delete_responce.text
    assert delete_text==""


logger.info("First test case for put")
def test_put_1():
    statuscode=put_responce.status_code
    assert statuscode==200
#failed test case


logger.info("Second test case for put")
def test_put_2():
    text = json.loads(put_responce.text)
    var_name = jsonpath.jsonpath(text, "name")
    assert var_name[0]=="bot"


