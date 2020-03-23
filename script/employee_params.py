import logging

import pymysql

import app
import requests
import unittest
from api.emp_api import EmployeeApi
from utils import assert_common_utils, read_add_emp, read_query_emp, read_modify_emp, read_delete_emp
from parameterized.parameterized import parameterized


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp_api=EmployeeApi()

    def tearDown(self):
        pass

    def test01_login_success(self):
        app.init_logging()
# 获取令牌
        response = self.emp_api.login("13800000002", "123456")
        logging.info("员工模块登录结果为:{}".format(response.json()))
        token = "Bearer " + response.json().get("data")
        logging.info("取出令牌为{}".format(token))
        headers = {"Content-Type": "application/json", "Authorization": token}
        app.HEADRES=headers
        logging.info("员工请求模块为:{}".format(app.HEADRES))
# 增
    @parameterized.expand(read_add_emp)
    def test03_add_emp(self,username,mobile,http_code,success,code,message):
        response_add_emp=self.emp_api.add_emp(username,mobile,app.HEADRES)
        logging.info("添加员工接口结果为:{}".format(response_add_emp.json()))
        assert_common_utils(self,response_add_emp,http_code, success, code,message)
# # 获取员工指定id
        emp_id = response_add_emp.json().get("data").get("id")
        app.EMP_ID=emp_id
        logging.info("保存的员工ID为:{}".format(app.EMP_ID))

# 查
    @parameterized.expand(read_query_emp)
    def test04_query(self,http_code,success,code,message):
        response_query = self.emp_api.emp_query(app.EMP_ID,headers=app.HEADRES)
        logging.info("查询员工结果为:{}".format(response_query.json()))
        assert_common_utils(self,response_query,http_code,success,code,message)

# 链接数据库查询
#         conn=pymysql.connect(host="182.92.81.159",
#                              user="readuser",
#                              password="iHRM_USER_2019",
#                              database="ihem")
#         cursor=conn.cursor()
#         sql="setect username from where id={}".format(app.EMP_ID)
#         logging.info("要查询的的sql语句为:{}".format(sql))
#         cursor.execute(sql)
#         result=cursor.fetchone()
#         logging.info("sql查询的结果为:{}".format(result))
#         self.assertEqual("王健林12349",result[0])
#         cursor.close()
#         conn.close()
# 改
    @parameterized.expand(read_modify_emp)
    def test05_modify(self,username,http_code,success,code,message):
        response_modify =self.emp_api.emp_modify(app.EMP_ID,username,app.HEADRES)
        logging.info("修改员工结果为:{}".format(response_modify.json()))
        assert_common_utils(self, response_modify,http_code,success,code,message)
# 删
    @parameterized.expand(read_delete_emp)
    def test06_delete(self,http_code,success,code,message):
        response_delete = self.emp_api.delete_emp(app.EMP_ID,app.HEADRES)
        logging.info("删除员工结果为:{}".format(response_delete.json()))
        assert_common_utils(self, response_delete,http_code,success,code,message)