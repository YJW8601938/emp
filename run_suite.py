import os
import unittest

import time

from script.employee_params import TestEmployee
from script.login_params import TestLogin

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))

report_path=os.path.dirname(os.path.abspath(__file__))+"/report/ihrm{}.html".format(time.strftime("%Y%m%d  %H%M%S"))
with open(report_path ,mode="wb") as f:
    from HTMLTestRunner_PY3 import HTMLTestRunner
    runner=HTMLTestRunner(f , verbosity=2,title="人力资源接口测试报告",description="这是项目实战的报告")
    runner.run(suite)