import os
import unittest
from BeautifulReport import BeautifulReport
from config.config import case_path,report_path

# dir_path=os.getcwd()+'\testcases' #获取当前文件的目录
# print(dir_path)
# print(os.path.dirname(dir_path))
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(unittest_framework))
# suite.addTest(loader.discover(start_dir=case_path,pattern='test*.py'))
cases=unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')
# runner=unittest.TextTestRunner()
# runner.run(suite)
##运用BeautifulReport执行器，执行测试用例
result=BeautifulReport(cases)
##生成html的测试报告
result.report(description='自动化测试',filename='SIT测试',report_dir=report_path)