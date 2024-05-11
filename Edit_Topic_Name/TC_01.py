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

WebDriverWait(driver, WAIT_TIME).until(
  EC.presence_of_element_located((By.XPATH, '//input[@class="custom-control-input"]'))
)

driver.find_element(By.XPATH, '//input[@class="custom-control-input"]').click()

WebDriverWait(driver, WAIT_TIME).until(
  EC.presence_of_element_located((By.CSS_SELECTOR, '#sectionid-547-title .icon'))
)

driver.find_element(By.CSS_SELECTOR, '#sectionid-547-title .icon').click()

WebDriverWait(driver, WAIT_TIME).until(
  EC.presence_of_element_located((By.XPATH, '//input[@class="ignoredirty form-control"]'))
)

driver.find_element(By.XPATH, '//input[@class="ignoredirty form-control"]').send_keys('Hello World' + Keys.ENTER)

driver.find_element(By.XPATH, '//input[@class="custom-control-input"]').click()

try:
  driver.find_element(By.LINK_TEXT, 'Hello World')
  print('Success')
except:
  print('Fail')

time.sleep(10)
driver.quit()