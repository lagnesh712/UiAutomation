from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from csv import DictWriter
from pynput.keyboard import Key ,Controller




service_obj= Service("/home/lagnesh/interview_practice/utility/chromedriver")

driver=webdriver.Chrome(service=service_obj)
# # Test Case 1:
# # Go to Google.com
# # Enter "IPL points table 2021" in search box
# # Capture all the Suggestions from the search box and store in List
# # Search for "ipl points table 2021" in list & Google it by Pressing Enter(Google Search) with use of Key Press
# driver.get("https://www.google.com")
# driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys("IPl points table 2021")
# wait=WebDriverWait(driver,10)
# wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//*[@class="G43f7e"]/li')))
# option_list=driver.find_elements(By.XPATH,'//*[@class="G43f7e"]/li')
# suggestions=[]
# for i in option_list:
#     suggestions.append(i.text)
# print(suggestions)
# driver.find_element(By.XPATH,'//*[@id="APjFqb"]').send_keys(Keys.ENTER)
# # Test Case 2:
# # Go To https://www.iplt20.com/points-table/men/2021
# # From the Points Table Get Details of Team(Rank ,Team Name , Points) who has Points greater than 8.
# # Store the captured details in CSV file.
# driver.get("https://www.iplt20.com/points-table/men/2021")
# teams=driver.find_elements(By.XPATH,'//*[@id="pointsdata"]/tr')
# rank=0
# with open('data.csv','w') as f:
#     csv_writer=DictWriter(f,fieldnames=["Rank","Team Name", "Points"])
#     csv_writer.writeheader()
#     for i in teams:
#         points=int(i.find_element(By.XPATH,'td[11]').text)
#         if points>8:
#             rank=rank+1
#             csv_writer.writerow({
#                 "Rank":rank,
#                 "Team Name":(i.find_element(By.XPATH,'td[3]/div/h2').text),
#                 "Points":points
#             })
# f.close()

# Test Case 3:
# Upload Test Case-2 Result CSV file on https://www.zamzar.com/convert/csv-to-pdf/
# Convert into PDF using website engine.
# Download and Save the PDF file on Desktop.
driver.get("https://www.zamzar.com/convert/csv-to-pdf/#")
driver.find_element(By.XPATH,'//*[@id="btn-dd"]').click()
driver.find_element(By.XPATH,'//*[text()="From my computer"]').click()
keyboard= Controller()
keyboard.type('/home/lagnesh/selenium/test/data.csv')
keyboard.press(Key.enter)
keyboard.release(Key.enter)
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//*[@id="convert"]')))
print("line1")
driver.find_element(By.XPATH,'//*[@id="convert"]').click()
print("line2")
time.sleep(3)
print("line3")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[text()="Download"]')))
print("line4")
driver.find_element(By.XPATH,'//*[text()="Download"]').click()
print("line4")
    
