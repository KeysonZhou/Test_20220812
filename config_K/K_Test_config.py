import os

raw_path=os.path.dirname(__file__)
root_path=os.path.dirname(raw_path)
data_path=root_path+'\\Test_data\\testdata.txt'
result_path=root_path+'\\Test_result'
driver_path=root_path+'\\driver\\chromedriver.exe'
log_path=root_path+'\\log\\log.txt'
cases_path=root_path+'\\unittest_m'
file_path=root_path+'\\Test_data\\K_Test_Data.xlsx'

# print(raw_path)
# print(root_path)
# print(data_path)
# print(result_path)
# print(driver_path)
# print(log_path)

url="http://127.0.0.1/index.php"