import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
from faker import Faker

fake = Faker()

name = "Anna"
surname = "Nowak"
country = "United States"
phone = "123456789"
email = fake.email()
password = "12345"


class WizzairRegistration(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    def testIncorrectEmail(self):

        # Kliknij "Zaloguj się"
        signin = self.driver.find_element_by_xpath("/html/body/div[2]/div/header/div[1]/div/nav/ul/li[11]/button")
        signin.click()

        # Kliknij "Rejestracja"
        registration = self.driver.find_element_by_xpath("/html/body/div[2]/span/article/div/div/div/form/p/button")
        registration.click()

        # Wpisz imię
        name_input = self.driver.find_element_by_xpath("/html/body/div[2]/span/article/div/div/div/form/div[2]/div[1]/label[1]/div[1]/input")
        name_input.send_keys(name)

        # Wpisz nazwisko
        surname_input = self.driver.find_element_by_xpath("/html/body/div[2]/span/article/div/div/div/form/div[2]/div[1]/label[2]/div[1]/input")
        surname_input.send_keys(surname)

        # Wybierz płeć
        gender_female = self.driver.find_element_by_xpath("/html/body/div[2]/span/article/div/div/div/form/div[3]/div[1]/label[1]/span")
        gender_female.click()

        # Wybierz kod kraju



        # Wpisz numer
        phone_input = self.driver.find_element_by_xpath("/html/body/div[2]/span/article/div/div/div/form/div[4]/div[2]/div/div[1]/div/label/input")
        phone_input.send_keys(phone)

        time.sleep(2)

        print("OK")

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)