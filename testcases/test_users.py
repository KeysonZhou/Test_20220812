import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.config import d_path,url

class UserCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("打开浏览器")
        driver_path = Service(executable_path=d_path)  # 获取浏览器的路径
        cls.browser = webdriver.Chrome(service=driver_path)  # 打开浏览器、
        # sleep(3)
        cls.browser.maximize_window()  # 最大化页面
        cls.browser.get(url)  # 访问url
    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        sleep(2)
        cls.browser.quit()

    def setUp(self):
        print("输入数据")
        sleep(2)
        self.browser.find_element(By.CSS_SELECTOR, "#account").send_keys("shelly")  # 元素位置By.ID+操作
        self.browser.find_element(By.CSS_SELECTOR, "[name='password']").send_keys("p@ssw0rd")
        self.browser.find_element(By.CSS_SELECTOR, "#submit").click()
        sleep(1)

    def tearDown(self):
        print("清除数据")
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'user-name')))
        self.browser.find_element(By.CLASS_NAME, 'user-name').click()
        self.browser.find_element(By.LINK_TEXT, '退出').click()

    @unittest.skip
    def test_a_add_user(self):   #实例方法是测试用例
        print("成功添加用户")
        '''
        验证成功添加用户
        '''
        self.browser.find_element(By.LINK_TEXT,'组织').click()
        self.browser.find_element(By.LINK_TEXT,'添加用户').click()
        self.browser.find_element(By.ID,'account').send_keys("test7_29_1")
        self.browser.find_element(By.ID,'password1').send_keys('p@ssw0rd')
        self.browser.find_element(By.ID,'password2').send_keys('p@ssw0rd')
        self.browser.find_element(By.ID,'realname').send_keys(u'中文')
        from selenium.webdriver.support.select import Select
        elem=self.browser.find_element(By.ID,'role')  #定位select元素
        Select(elem).select_by_value('qd')  #Select（elem）实例化一个select的对象，调用实例方法select_by_value()
        #滚动条
        js='var q=document.documentElement.scrollTop=1000'
        self.browser.execute_script(js)
        self.browser.find_element(By.ID,'verifyPassword').send_keys("p@ssw0rd")
        self.browser.find_element(By.ID,'submit').click()
        sleep(2)

    @unittest.skip
    def test_b_search_user(self):
        print('搜索用户')
        '''
        验证搜索用户
        '''
        sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, 'a[href$="company/"').click()
        self.browser.find_element(By.CSS_SELECTOR, 'a[href$="company-browse.html"]').click()
        sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, "#bysearchTab").click()
        sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, '#value1').send_keys(u'中文')
        self.browser.find_element(By.CSS_SELECTOR, '#submit').click()
        sleep(2)
        elems = self.browser.find_elements(By.CSS_SELECTOR, "#userList>tbody>tr")  # 获取列表类型数据
        assert len(elems) >= 1, '搜索失败'

    @unittest.skip
    def test_c_delete_user(self):
        '''
        验证删除用户
        '''
        sleep(3)
        # self.browser.find_element(By.CLASS_NAME,'icon-trash').click()
        self.browser.find_element(By.CSS_SELECTOR, 'a[href$="company/"').click()
        self.browser.find_element(By.CSS_SELECTOR, 'a[href$="company-browse.html"]').click()
        self.browser.find_element(By.CSS_SELECTOR, "#bysearchTab").click()
        sleep(1)
        self.browser.find_element(By.CSS_SELECTOR, '#value1').send_keys(u'中文')
        self.browser.find_element(By.CSS_SELECTOR, '#submit').click()
        sleep(3)
        self.browser.find_element(By.XPATH,'//table[@id="userList"]/tbody/tr[1]/td[11]/a[2]/i').click()
        sleep(3)
        # self.browser.find_element(By.CLASS_NAME, 'icon-trash').click()
        sleep(2)
        self.browser.switch_to.frame(1)
        self.browser.find_element(By.ID,'verifyPassword').send_keys('p@ssw0rd')
        self.browser.find_element(By.ID,'submit').click()
        self.browser.switch_to.parent_frame()
        sleep(3)


if __name__=='__main__':
    unittest.main()