import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WebTesting:
    def __init__(self):
        self.search_element = None
        self.driver = webdriver.Chrome(service=webdriver.ChromeService("./Drivers/chromedriver.exe"))

    def driver_initialization(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()

    def first_test(self):
        self.search_element = self.driver.find_element(By.XPATH, "//textarea[@class='gLFyf']")
        self.search_element.send_keys("Python")
        self.search_element.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//h3[contains(text(),'Welcome to Python.org')]").click()
        get_title = self.driver.title
        assert get_title == "Welcome to Python.org"

    def teardown(self):
        time.sleep(2)
        self.driver.close()
        self.driver.quit()


class_instance = WebTesting()
class_instance.driver_initialization()
class_instance.first_test()
class_instance.teardown()
