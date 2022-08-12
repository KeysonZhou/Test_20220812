import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config import d_path,url,file
from data.data import TestData
from pageobject.loginpage import LoginObject
from log.log import logger
class LoginCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        driver_path = Service(executable_path=d_path)  # 获取浏览器的路径
        cls.browser = webdriver.Chrome(service=driver_path)  # 打开浏览器、
        # sleep(3)
        cls.browser.maximize_window()  # 最大化页面
        cls.browser.get(url)  # 访问url
        cls.page=LoginObject(cls.browser)
    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        cls.browser.quit()

    # @unittest.skip
    def test_login_a_success(self):   #实例方法是测试用例
        print("成功登录系统")
        '''
        验证用户成功登录
        '''
        t_data=TestData(file,'login')
        list_data=t_data.read_xls()
        username=list_data[0][0]
        password=list_data[0][1]
        self.page.input_username(username)  # 元素位置By.ID+操作
        self.page.input_password(password)
        self.page.click_login()
        logger.info('用户登录成功')
        sleep(1)
        # assert self.browser.title == "我的地盘 - 禅道", "登录页面打开失败"
        self.assertEqual(self.browser.title,"我的地盘 - 禅道",msg="登录页面打开失败")
        WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,'user-name')))
        self.page.click_logout()
        logger.info('用户成功退出')

    @unittest.skip
    def test_login_b_unsuccess(self):
        print('异常数据登录系统')
        '''
        验证不存在用户登录
        '''
        sleep(3)
        t_data = TestData(file, 'login')
        list_data = t_data.read_xls()
        username = list_data[1][0]
        password = list_data[1][1]
        self.page.input_username(username)  # 元素位置By.ID+操作
        self.page.input_password(password)
        self.page.click_login()
        sleep(2)
        if EC.alert_is_present():
            alert=self.browser.switch_to.alert
            alert.accept()


if __name__=='__main__':
## POM :page object model
    unittest.main()