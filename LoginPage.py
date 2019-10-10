
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = "//input[@name='userName']"
        self.password = "//input[@name='password']"
        self.login_btn = "//input[@name='login']"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username).clear()
        self.driver.find_element_by_xpath(self.username).send_keys(username)
        self.driver.implicitly_wait(5)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password).clear()
        self.driver.find_element_by_xpath(self.password).send_keys(password)
        self.driver.implicitly_wait(5)

    def login_click(self):
        self.driver.find_element_by_xpath(self.login_btn).click()
        self.driver.implicitly_wait(10)
