from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.google.pl")
element = driver.find_element_by_name("q")
element.send_keys("Test Automation")
element.submit()
time.sleep(2)
driver.close()

