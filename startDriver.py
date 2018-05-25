from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import unittest
import time

class Test(unittest.TestCase):

    def setUp(self):
        url = 'https://mail.rediff.com/cgi-bin/login.cgi'
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def test_popup(self):
        driver = self.driver
        btn = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div/form/div/div[6]/div[1]/input'))
        # btn = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div/form/div/div[6]/div[1]/input')
        btn.click()
        s = driver.switch_to.alert.text
        a= driver.switch_to.alert.accept()
        driver.implicitly_wait(5000)

        assert s == 'Please enter a valid user name'

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

# test_popUp()

# if __name__ == '__main__':
#     HtmlTestRunner.main()
