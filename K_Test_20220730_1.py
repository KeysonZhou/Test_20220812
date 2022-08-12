from BeautifulReport import  BeautifulReport      #导入第三方模块用于报告
import unittest
from config_K.K_Test_config import cases_path,result_path

suite=unittest.TestSuite()
# # 使用loader进行测试用例加载
loader=unittest.TestLoader()
## 使用框架加载测试用例
# # cases_1=loader.loadTestsFromModule(K_Test_Login)
# ##使用文件方式加载测试用例
cases_2=loader.discover(start_dir=cases_path,pattern='K_Test_*.py')
suite.addTest(cases_2)
#
##使用BeautifulReport输出测试用例结果
result=BeautifulReport(suite)
#
result.report(description='自动化测试练习',filename='自动化框架练习测试',report_dir=result_path)


# TestRunner=unittest.TextTestRunner()
# ##执行用例集
# TestRunner.run(suite)