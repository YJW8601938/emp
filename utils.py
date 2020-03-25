import json
import os


def assert_common_utils(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

def read_login_data():
    login_data_path=os.path.dirname(os.path.abspath(__file__))+"/data/login.json"
    with open(login_data_path,mode="r",encoding="utf-8") as f:
        jsonData=json.load(f)
        result_list=[]
        for case_data in jsonData:
            mobile=case_data.get("mobile")
            password=case_data.get("password")
            http_code=case_data.get("http_code")
            success=case_data.get("success")
            code=case_data.get("code")
            message=case_data.get("message")
            result_list.append((mobile,password,http_code,success,code,message))

        print("读取出来的数据为:",result_list)

        return result_list

        # 增
def read_add_emp():
    emp_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    with open(emp_path,mode="r",encoding="utf-8") as f:
        jsonData=json.load(f)#type:dict
        result_list=[]
        add_emp_data=jsonData.get("add_emp")

        username=add_emp_data.get("username")
        mobile=add_emp_data.get("mobile")
        http_code=add_emp_data.get("http_code")
        success=add_emp_data.get("success")
        code=add_emp_data.get("code")
        message=add_emp_data.get("message")
        result_list.append((username,mobile,http_code,success,code,message))
    print("读取员工的数据为:",result_list)
    return result_list


def read_query_emp():
    emp_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    with open(emp_path,mode="r",encoding="utf-8") as f:
        jsonData=json.load(f)#type:dict
        result_list=[]
        add_emp_data=jsonData.get("query_emp")

        username=add_emp_data.get("username")
        mobile=add_emp_data.get("mobile")
        http_code=add_emp_data.get("http_code")
        success=add_emp_data.get("success")
        code=add_emp_data.get("code")
        message=add_emp_data.get("message")
        result_list.append((http_code,success,code,message))
    print("读取员工的数据为:",result_list)
    return result_list

def read_modify_emp():
    emp_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    with open(emp_path,mode="r",encoding="utf-8") as f:
        jsonData=json.load(f)#type:dict
        result_list=[]
        add_emp_data=jsonData.get("modify_emp")

        username=add_emp_data.get("username")
        http_code=add_emp_data.get("http_code")
        success=add_emp_data.get("success")
        code=add_emp_data.get("code")
        message=add_emp_data.get("message")
        result_list.append((username,http_code,success,code,message))
    print("读取员工的数据为:",result_list)
    return result_list

def read_delete_emp():
    emp_path=os.path.dirname(os.path.abspath(__file__))+"/data/employee.json"
    with open(emp_path,mode="r",encoding="utf-8") as f:
        jsonData=json.load(f)#type:dict
        result_list=[]
        add_emp_data=jsonData.get("delete_emp")

        http_code=add_emp_data.get("http_code")
        success=add_emp_data.get("success")
        code=add_emp_data.get("code")
        message=add_emp_data.get("message")
        result_list.append((http_code,success,code,message))
    print("读取员工的数据为:",result_list)
    return result_list


if __name__ == '__main__':
    read_login_data()
    # read_add_emp()
    # read_query_emp()
    # read_modify_emp()