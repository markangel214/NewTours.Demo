class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_off_btn = "//a[contains(text(),'SIGN-OFF')]"

    def logout(self):
        self.driver.find_element_by_xpath(self.sign_off_btn).click()

