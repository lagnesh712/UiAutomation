from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
import time
from selenium.webdriver.support.wait import WebDriverWait
service_obj=Service('/home/lagnesh/interview_practice/utility/chromedriver')

driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.XPATH,'//*[text()="Register"]')))
driver.find_element(By.XPATH,'//*[text()="Register"]').click()
driver.find_element(By.ID,'firstName').send_keys("Lagnesh")
driver.find_element(By.ID,'lastName').send_keys("Chouhan")
driver.find_element(By.ID,'userEmail').send_keys("lagneshcivil@gmail.com")
driver.find_element(By.ID,'userMobile').send_keys("877075545")
dropdown=Select(driver.find_element(By.XPATH,'//*[@formcontrolname="occupation"]'))
dropdown.select_by_visible_text("Engineer")
time.sleep(3)