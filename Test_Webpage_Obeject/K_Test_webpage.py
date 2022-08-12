from selenium.webdriver.common.by import By


class LoginObeject():
    def __init__(self,boweser):
        self.driver=boweser
        self.p_username=By.ID, "account"                                     #用户名路径
        self.p_password=By.NAME, "password"                                  #密码路径
        self.p_login=By.ID, "submit"                                         #登录按钮路径
        self.p_surface_login=By.LINK_TEXT, '开源版'                           #'开源'按钮路径
        self.p_logout_main_page=By.XPATH, '/html/body/div[1]/nav[1]/ul[1]/li[1]/a'  #主页面路径
        self.p_logout_main_frame='appIframe-my'                              #用户选项所在框架（或页面）名
        self.p_logout_user_name = By.ID, 'main-avatar'                       #用户选项按钮路径
        self.p_logout_button = By.LINK_TEXT, '退出'                        #退出按钮路径


    def enter_surface_login(self):                                           #点击'开源'按钮进入登录界面
        self.driver.find_element(*self.p_surface_login).click()

    def input_username(self,username):                                      #输入用户名
        self.driver.find_element(*self.p_username).send_keys(username)

    def input_password(self,password):                                      #输入用密码
        self.driver.find_element(*self.p_password).send_keys(password)

    def click_login(self):                                                  #点击登录按钮
        self.driver.find_element(*self.p_login).click()

    def click_logout(self):
        self.driver.find_element(*self.p_logout_main_page).click()
        self.driver.switch_to.frame(self.p_logout_main_frame)
        self.driver.find_element(*self.p_logout_user_name).click()
        self.driver.find_element(*self.p_logout_button).click()


