import unittest , logging,requests

from parameterized.parameterized import parameterized

from api.login_api import LoginApi
from utils import assert_common_utils, read_login_data


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass


    # 登录测试函数

    # 登录成功
    @parameterized.expand(read_login_data)
    def test01_login(self,mobile,password,http_code,success,code,message):
        response=self.login_api.login(mobile,password)
        logging.info("参数化登陆的结果为{}".format(response.json()))

        assert_common_utils(self,response,http_code,success,code,message)