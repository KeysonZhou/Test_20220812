import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
import datetime
from config_K.K_Test_config import driver_path,url,file_path
from Test_Webpage_Obeject.K_Test_webpage import LoginObeject
from Test_Data.K_Test_Data import TestData

class Test_users(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''打开浏览器'''
        print('打开浏览器')
        cls.driver_path = Service(executable_path=driver_path)
        cls.browser = webdriver.Chrome(service=cls.driver_path)
        cls.browser.maximize_window()
        cls.browser.get(url)
        cls.webpage = LoginObeject(cls.browser)
        cls.webpage.enter_surface_login()

    @classmethod
    def tearDownClass(cls):
        '''关闭浏览器'''
        print("关闭浏览器")
        cls.browser.close()    #关闭浏览器

    def setUp(self):
        '''登录系统'''
        get_data = TestData(file_path, 'login')
        user_data = get_data.read_xlsx()
        username = user_data[0][0]
        pw = user_data[0][1]

        self.browser.implicitly_wait(10)  # 隐式等待
        self.webpage.input_username(username)
        self.webpage.input_password(pw)
        self.webpage.click_login()

    def tearDown(self) -> None:
        '''退出系统'''
        self.webpage.click_logout()

    def test_a_Add_user(self):
        '''添加用户'''
        self.browser.implicitly_wait(3)  # 隐式等待
        self.browser.find_element(By.XPATH, '/html/body/div[1]/nav[1]/ul[1]/li[13]/a').click()
        sleep(1)
        self.browser.switch_to.frame('appIframe-admin')
        self.browser.find_element(By.LINK_TEXT, '人员').click()
        # 添加用户
        self.browser.find_element(By.LINK_TEXT, '添加用户').click()
        self.browser.find_element(By.ID, 'account').send_keys('tester_'+str(datetime.datetime.now().strftime('%m%d%H%M%S')))
        self.browser.find_element(By.ID, 'password1').send_keys('Tester020')
        self.browser.find_element(By.ID, 'password2').send_keys('Tester020')
        self.browser.find_element(By.ID, 'realname').send_keys(u'测试072201')
        elem = self.browser.find_element(By.ID, 'role')  # 定位select元素
        Select(elem).select_by_value('dev')  # Select（elem）实例化一个select的对象，调用实例方法select_by_value()
        self.browser.find_element(By.ID, 'email').send_keys('test@163.com')
        self.browser.find_element(By.ID, 'commiter').send_keys('testcode')
        self.browser.find_element(By.ID, 'genderm').click()
        self.browser.find_element(By.ID,'verifyPassword').send_keys('Hs349870333')
        self.browser.find_element(By.ID,'submit').click()
        self.browser.switch_to.default_content()

    def test_b_Delete_user(self):
        '''删除用户'''
        self.browser.implicitly_wait(3)  # 隐式等待
        self.browser.find_element(By.XPATH, '/html/body/div[1]/nav[1]/ul[1]/li[13]/a').click()
        self.browser.switch_to.frame('appIframe-admin')
        self.browser.find_element(By.LINK_TEXT, '人员').click()
        self.browser.find_element(By.LINK_TEXT, '搜索').click()
        self.browser.find_element(By.ID,'value1').send_keys('测试')
        self.browser.find_element(By.ID,'submit').click()
        sleep(1)
        self.browser.find_element(By.XPATH,'//table[@id="userList"]/tbody/tr[1]/td[11]/a[2]/i').click()
        self.browser.switch_to.frame('iframe-triggerModal')
        self.browser.find_element(By.ID,'verifyPassword').send_keys('Hs349870333')
        self.browser.find_element(By.ID,'submit').click()
        self.browser.switch_to.default_content()


if __name__=='__main__':
    unittest.main()


