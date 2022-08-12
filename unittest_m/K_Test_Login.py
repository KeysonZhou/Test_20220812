import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC   #条件判断
from config_K.K_Test_config import driver_path,url,file_path
from Test_Data.K_Test_Data import TestData
from Test_Webpage_Obeject.K_Test_webpage import LoginObeject
from log.K_Test_log import logger

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''打开浏览器'''
        print('打开浏览器')
        cls.driver_path = Service(executable_path=driver_path)
        cls.browser = webdriver.Chrome(service=cls.driver_path)
        cls.browser.maximize_window()
        cls.browser.get(url)
        cls.webpage=LoginObeject(cls.browser)
        cls.webpage.enter_surface_login()

    @classmethod
    def tearDownClass(cls):
        '''关闭浏览器'''
        print("关闭浏览器")
        cls.browser.close()    #关闭浏览器

    def test_Login_a_success(self):
        '''成功登录验证'''
        print('成功登录系统')
        get_data=TestData(file_path,'login')
        user_data=get_data.read_xlsx()
        username=user_data[0][0]
        pw=user_data[0][1]


        self.browser.implicitly_wait(10)                                #隐式等待
        self.webpage.input_username(username)
        self.webpage.input_password(pw)
        self.webpage.click_login()
        logger.info('用户登录成功')
        sleep(1)
        assert self.browser.title == '地盘 - 禅道', '登录页面打开失败'  # 表达式为真时，继续执行程序；表达式为假时，触发输出
        # self.browser.switch_to.parent_frame()  # 返回上一层，此处可用可不用
        # self.browser.switch_to.frame(1)

        self.webpage.click_logout()
        logger.info('用户成功退出')

    # @unittest.skip
    def test_Login_b_failed(self):
        '''错误登录验证'''
        print('错误登录系统')
        get_data = TestData(file_path, 'login')
        user_data = get_data.read_xlsx()
        username = user_data[1][0]
        pw = user_data[1][1]
        self.browser.implicitly_wait(3)  # 隐式等待
        self.webpage.input_username(username)
        self.webpage.input_password(pw)
        self.webpage.click_login()
        sleep(1)
        if EC.alert_is_present():
            self.alert_t=self.browser.switch_to.alert
            content=self.alert_t.text
            print(content)
            self.alert_t.accept()


if __name__=='__main__':
    unittest.main()