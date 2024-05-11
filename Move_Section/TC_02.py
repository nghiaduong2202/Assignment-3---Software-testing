from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

WAIT_TIME = 10

service = Service(executable_path="../chromedriver.exe")
driver = webdriver.Chrome(service=service)

# login page
driver.get('https://school.moodledemo.net/login/index.php?loginredirect=1')
WebDriverWait(driver, WAIT_TIME).until(
  EC.presence_of_element_located((By.ID, "username"))
)

username = driver.find_element(By.ID, "username")
username.send_keys("teacher")

password = driver.find_element(By.ID, "password")
password.send_keys("moodle" + Keys.ENTER)

WebDriverWait(driver, WAIT_TIME).until(
  EC.presence_of_element_located((By.LINK_TEXT, "Moodle and Mountaineering"))
)

driver.find_element(By.LINK_TEXT, "Moodle and Mountaineering").click()

try:
  driver.find_element(By.ID, 'action-menu-toggle-6')
  print('Fail')
except:
  print('Success')

time.sleep(10)
driver.quit()