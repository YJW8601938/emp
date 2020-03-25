import unittest , logging,requests
from api.login_api import LoginApi
from utils import assert_common_utils


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api=LoginApi()
    def tearDown(self):
        pass


    # 登录测试函数

    # 登录成功
    def test01_login_success(self):
        response=self.login_api.login("13800000002","123456")
        logging.info("登陆成功的结果为{}".format(response.json()))

        assert_common_utils(self,response,200,True,10000,"操作成功")

    # 用户名不存在
    def test02_username_is_not_exist(self):
        response = self.login_api.login("13900000002", "123456")
        logging.info("用户名不存在登陆的结果为{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")

    # 密码错误
    def test03_password_is_error(self):
        response = self.login_api.login("13800000002", "error")
        logging.info("密码错误登陆的结果为{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 无参
    def test04_none_params(self):
        response = requests.post('http://182.92.81.159/api/sys/login')
        logging.info("无参的结果为：{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！")
    # 用户名为空
    def test05_username_is_null(self):
        response = self.login_api.login("","1234567")
        logging.info("用户名为空登陆的结果为{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 密码为空
    def test06_password_is_null(self):
        response = self.login_api.login("13800000002", "")
        logging.info("密码为空登陆的结果为{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参mobile
    def test07_less_mobile(self):
        response = self.login_api.login_params({"password":"123456"})
        logging.info("少参的结果为：{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 少参password
    def test08_less_password(self):
        response = requests.post('http://182.92.81.159/api/sys/login',json={"mobile":"13800000002"})
        logging.info("无参的结果为：{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")
    # 多参
    def test09_add_params(self):
        response = requests.post('http://182.92.81.159/api/sys/login',json={"mobile":"13800000002",
                                                                            "password": "123456",
                                                                            "add":"add"})
        logging.info("多参登录的结果为{}".format(response.json()))

        assert_common_utils(self,response,200,True,10000,"操作成功")
    # 错误参
    def test010_error_params(self):
        response = requests.post('http://182.92.81.159/api/sys/login',json={"mbile":"13800000002",
                                                                            "password": "123456",
                                                                            })
        logging.info("错误参数的结果为：{}".format(response.json()))

        assert_common_utils(self, response, 200, False, 20001, "用户名或密码错误")