from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
import time

service_obj=Service('/home/lagnesh/interview_practice/utility/chromedriver')

driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[text()="Email"]//following-sibling::input').send_keys("lagneshcivil@gmail.com")
driver.find_element(By.XPATH,'//*[text()="Password"]//following-sibling::input').send_keys("jaibarfani")
driver.find_element(By.ID,'login').click()
time.sleep(3)