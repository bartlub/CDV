import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
from faker import Faker

fake = Faker()

name = "Marcin"
surname = "Kowal"
birth_date = ["1", "12", "1987"]
company = "DRE"
address1 = "Waterfall Street 105"
address2 = "Apartment 2"
city = "New York"
state = "New York"
country = "United States"
postcode = "00000"
address_alias = "My address"
phone = "123 456 789"
email = fake.email()
password = "12345"


class TestRegistration(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def testCorrectRegistration(self):
        # Kliknij przycisk "Sign in"
        signin_button = self.driver.find_element_by_class_name("login")
        signin_button.click()

        # Wpisz adres email
        email_create = self.driver.find_element_by_id("email_create")
        email_create.send_keys(email)

        # Kliknij Create an account
        create_button = self.driver.find_element_by_id("SubmitCreate")
        create_button.click()

        # Wybierz tytuł (płeć)
        title_button = self.driver.find_element_by_id("id_gender1")
        title_button.click()

        # Wpisz imię
        first_name = self.driver.find_element_by_id("customer_firstname")
        first_name.send_keys(name)

        # Wpisz nazwisko
        last_name = self.driver.find_element_by_id("customer_lastname")
        last_name.send_keys(surname)

        # Sprawdź uzupełniony email
        email_input = self.driver.find_element_by_id("email")
        email_value = email_input.get_attribute("value")
        assert email_value == email

        # Podaj hasło
        password_input = self.driver.find_element_by_id("passwd")
        password_input.send_keys(password)

        # Wybierz datę urodzenia
        day = Select(self.driver.find_element_by_xpath('//select[@name="days"]'))
        day.select_by_value(birth_date[0])

        month = Select(self.driver.find_element_by_xpath('//select[@name="months"]'))
        month.select_by_value(birth_date[1])

        year = Select(self.driver.find_element_by_xpath('//select[@name="years"]'))
        year.select_by_value(birth_date[2])

        # Sprawdź uzupełnione imię
        first_name_2 = self.driver.find_element_by_id("firstname")
        first_name_2_value = first_name_2.get_attribute("value")
        assert first_name_2_value == name

        # Sprawdź uzupełnione nazwisko
        last_name_2 = self.driver.find_element_by_id("lastname")
        last_name_2_value = last_name_2.get_attribute("value")
        assert last_name_2_value == surname

        # Wpisz nazwę firmy
        # company_copy_full_xpath = self.driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div/form/div[2]/p[3]/input")
        # company_copy_xpath = self.driver.find_element_by_xpath('//*[@id="company"]')
        company_my_xpath = self.driver.find_element_by_xpath('//input[@id="company"]')
        company_my_xpath.send_keys(company)

        # Wpisz adres
        address1_input = self.driver.find_element_by_id("address1")
        address1_input.send_keys(address1)

        address2_input = self.driver.find_element_by_id("address2")
        address2_input.send_keys(address2)

        # Wpisz miasto
        city_input = self.driver.find_element_by_id("city")
        city_input.send_keys(city)

        # Wybierz stan
        state_select = self.driver.find_element_by_xpath('//select[@id="id_state"]/option[34]')
        state_select.click()

        # Wpisz kod pocztowy
        postcode_input = self.driver.find_element_by_id("postcode")
        postcode_input.send_keys(postcode)

        # Wybierz kraj
        country_select = self.driver.find_element_by_xpath('//select[@id="id_country"]/option[2]')
        country_select.click()

        # Wpisz kod pocztowy
        phone_input = self.driver.find_element_by_id("phone_mobile")
        phone_input.send_keys(phone)

        # Sprawdź alias adresu
        alias = self.driver.find_element_by_id("alias")
        alias_value = alias.get_attribute("value")
        assert alias_value == address_alias

        # Kliknij "Register"
        submit_button = self.driver.find_element_by_id("submitAccount")
        submit_button.click()

        # Sprawdź czy konto zostało utworzone
        heading = self.driver.find_element_by_class_name("page-heading")
        assert heading.is_displayed() and heading.text == "MY ACCOUNT"

        time.sleep(2)

        print("Test passed - account created successfully")

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
