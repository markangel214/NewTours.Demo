import unittest
from selenium import webdriver
from Drivers import driver
from POM.Pages.LoginPage import LoginPage
from POM.Pages.HomePage import HomePage
from POM.Test.Print import Print
import HtmlTestRunner

class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("The Test Starting....\n")
        self.driver = webdriver.Chrome(executable_path="/Users/admin3/Documents/notes/NewTours.Demo/Drivers/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login(self):
        driver = self.driver
        driver.get("http://newtours.demoaut.com")
        printt = Print()
        login = LoginPage(driver)
        printt.print1(), login.enter_username("mercury"), printt.print11()
        printt.print2(), login.enter_password("mercury"), printt.print22()
        printt.print3(), login.login_click(), printt.print33()

        homepage = HomePage(driver)
        print("\nTitle of the Homepage"+str(driver.title))
        self.assertEqual("Find a Flight: Mercury Tours:", driver.title)
        self.driver.save_screenshot("/Users/admin3/Documents/notes/NewTours.Demo/ScreenShots/Homepage.jpg")
        printt.print4(), homepage.logout(), printt.print44()
        '''
        homepage = HomePage(driver)
        atitle = homepage.title()
        print(type(atitle))
        # self.assertEqual(str(title), "Find a Flight: Mercury Tours:", "The title is True")
        '''

    def tearDown(self):
        print("Goes to the Teardown Class!!!")
        self.driver.close()
        self.driver.quit()
        print("Test Complete!!!")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/admin3/Documents/notes/NewTours.Demo/Reports"), verbosity=2)
