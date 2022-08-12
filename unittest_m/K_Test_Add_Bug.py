import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
#强制等待
from selenium.webdriver.common.action_chains import ActionChains     #鼠标操作
from selenium.webdriver.common.keys import Keys    #键盘操作
from selenium.webdriver.support.ui import WebDriverWait   #显示等待
from selenium.webdriver.support import expected_conditions as EC   #条件判断
from config_K.K_Test_config import driver_path,url,data_path,file_path
from Test_Data.K_Test_Data import TestData
from Test_Webpage_Obeject.K_Test_webpage import LoginObeject

import win32gui                                       #window系统窗口三方库导入
import win32con
import os


class Test_Bugs(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        '''打开浏览器'''
        print('打开浏览器')
        cls.d_path = Service(executable_path=driver_path)
        cls.browser = webdriver.Chrome(service=cls.d_path)
        cls.browser.maximize_window()
        cls.browser.get(url)
        cls.webpage = LoginObeject(cls.browser)
        cls.webpage.enter_surface_login()

    @classmethod
    def tearDownClass(cls):
        '''关闭浏览器'''
        print("关闭浏览器")
        cls.browser.close()  # 关闭浏览器

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

    def test_add_Bug(self):
        '''禅道提交BUG'''

        # 进入提BUG页面
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/nav[1]/ul[1]/li[6]/a')))  # 显示等待
        self.browser.find_element(By.XPATH, '/html/body/div[1]/nav[1]/ul[1]/li[6]/a').click()
        self.browser.switch_to.frame('appIframe-qa')
        self.browser.find_element(By.LINK_TEXT, 'Bug').click()
        self.browser.find_element(By.LINK_TEXT, '提Bug').click()
        sleep(1)
        # 信息填写

        # 模块
        self.browser.find_element(By.XPATH, '//div[@id="moduleIdBox"]/div[1]/a').click()
        self.browser.find_element(By.XPATH, '//div[@id="moduleIdBox"]/div[1]/div/ul/li[2]').click()

        self.browser.find_element(By.ID, 'openedBuild_chosen').click()
        self.browser.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]/div/ul/li').click()

        self.browser.find_element(By.ID, 'deadline').send_keys('2022-08-30')

        self.browser.find_element(By.ID, 'typeBox').click()
        self.browser.find_element(By.XPATH, '//div[@id="type_chosen"]/div/ul/li[2]').click()

        self.browser.find_element(By.ID, 'os_chosen').click()
        self.browser.find_element(By.XPATH, '//div[@id="os_chosen"]/div/ul/li[2]').click()

        self.browser.find_element(By.ID, 'browser_chosen').click()
        self.browser.find_element(By.XPATH, '//div[@id="browser_chosen"]/div/ul/li[2]').click()

        self.browser.find_element(By.ID, 'title').send_keys('Bug提交测试')

        self.browser.find_element(By.XPATH, '//div[@class="input-group title-group required"]/div[2]/button').click()
        self.browser.find_element(By.XPATH,'//div[@class="input-group title-group required"]/div[2]/div/div/span[1]').click()

        self.browser.find_element(By.XPATH, '//div[@class="input-group title-group required"]/div[3]/button').click()
        self.browser.find_element(By.XPATH,'//div[@class="input-group title-group required"]/div[3]/div/div/span[1]').click()

        self.browser.switch_to.frame(0)
        self.browser.find_element(By.CLASS_NAME, 'article-content').clear()
        self.browser.find_element(By.CLASS_NAME, 'article-content').send_keys('[步骤]\nBug提交测试\n\n[结果]\nBug提交测试\n\n[期望\nBug提交测试')

        self.browser.switch_to.parent_frame()

        ##选择"抄送"方式一
        # browser.find_element(By.ID,'mailto_chosen').click()
        # browser.find_element(By.XPATH,'//div[@id="mailto_chosen"]/div/ul/li').click()

        # "抄送"方式二
        self.browser.find_element(By.ID, 'mailto_chosen').click()
        self.browser.find_element(By.XPATH, '//div[@id="mailto_chosen"]/ul/li/input').send_keys('admin')
        self.browser.find_element(By.XPATH, '//div[@id="mailto_chosen"]/ul/li/input').send_keys(Keys.ENTER)

        self.browser.find_element(By.ID, 'keywords').send_keys('Bug提交测试')

        # 上传文件
        self.browser.find_element(By.XPATH, '//div[@class="file-input-list"]/div/div[1]/button').click()
        sleep(1)
        win1 = win32gui.FindWindow('#32770', '打开')
        win2 = win32gui.FindWindowEx(win1, 0, 'ComboBoxEx32', None)
        win3 = win32gui.FindWindowEx(win2, 0, 'ComboBox', None)
        edit = win32gui.FindWindowEx(win3, 0, 'Edit', None)

        # dir_path = os.path.dirname(__file__)  # 获取当前文件的目录
        # dir_path_upper=os.path.dirname(dir_path)  #当前目录的上一级目录
        # dir_path_data = dir_path_upper+ '\\Test_data\\testdata.txt'

        # dir_path_data=r'D:\Python_Scripts\Web_Auto_Learning\Test_Data\testdata.txt'

        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, data_path)
        button = win32gui.FindWindowEx(win1, 0, 'Button', '打开(&O)')
        win32gui.SendMessage(win1, win32con.WM_COMMAND, 1, button)
        # self.browser.find_element(By.ID,'submit').click()               #提交Bug
        self.browser.switch_to.default_content()

if __name__=='__main__':
    unittest.main()