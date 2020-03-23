import requests
class EmployeeApi:
    def __init__(self):
        pass
    def login(self,mobile,password):
        login_uer="http://182.92.81.159/api/sys/login"
        jsonData={"mobile":mobile,"password":password}
        requests.post(login_uer,
                        json=jsonData)
        return requests.post(login_uer,
                        json=jsonData)

    def add_emp(self,username,mobile,headers):
        add_emp_url="http://182.92.81.159/api/sys/user"
        jsonDeta={"username":username,"mobile":mobile}
        response_add_emp = requests.post(add_emp_url,
                                         json={"username":username,
                                               "mobile": mobile,
                                               "timeOfEntry": "2020-02-01",
                                               "formOfEmployment": 1,
                                               "departmentName": "酱油2部",
                                               "departmentId": "1205026005332635648",
                                               "correctionTime": "2020-02-03T16:00:00.000Z"},
                                         headers=headers)
        return response_add_emp

    def emp_query(self,emp_id,headers):
        query_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_query = requests.get(query_url,headers=headers)
        return response_query

    def  emp_modify(self,emp_id,username,headers):
        modify_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_modify = requests.put(modify_url,
                                       json={"username": username},
                                       headers=headers)
        return response_modify

    def delete_emp(self, emp_id, headers):
        delete_url = "http://182.92.81.159/api/sys/user" + "/" + emp_id
        response_delete = requests.delete(delete_url, headers=headers)
        return response_delete

