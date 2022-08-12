from selenium.webdriver.common.by import By

class LoginObject:
    def __init__(self,driver):
        self.driver=driver
        self.p_username=By.CSS_SELECTOR, "#account"
        self.p_password=By.CSS_SELECTOR, "[name='password']"
        self.p_login=By.CSS_SELECTOR, "#submit"
        self.p_logout_user_name=By.CLASS_NAME,'user-name'
        self.p_logout_button=By.LINK_TEXT,'退出'

    def input_username(self,username):
        self.driver.find_element(*self.p_username).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(*self.p_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.p_login).click()

    def click_logout(self):
        self.driver.find_element(*self.p_logout_user_name).click()
        self.driver.find_element(*self.p_logout_button).click()