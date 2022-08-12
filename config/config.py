import os
# print(os.path.dirname(__file__))
root_path=os.path.dirname(os.path.dirname(__file__))

d_path=root_path+r'\driver\chromedriver.exe'
url="http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html"
case_path=root_path+r'\testcases'
report_path=root_path+r'\testresult'
file=root_path+r'\data\testdata.xlsx'
log_path=root_path+r'\log\log.txt'