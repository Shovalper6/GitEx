
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\Test\Desktop\chromedriver.exe")
driver.get("https://translate.google.com/")
translate = driver.find_element(By.CLASS_NAME, "er8xn")
translate.send_keys("חתול")
time.sleep(3)
translate = driver.find_element(By.CLASS_NAME,"er8xn")
translate.send_keys(Keys.BACK_SPACE*4)
time.sleep(2)
translate.send_keys("נמר מעופף")
time.sleep(3)
driver.close()