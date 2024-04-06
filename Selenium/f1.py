# " https://youtu.be/j7VZsCCnptM?si=-8h98OjFWA63J8DJ "

import os
from variable import *
from selenium import webdriver  # for UI automation 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#chrome driver - separate executable file that is used by selenium to perform the automated tasks on the Chrome browser
#driver_path="/Users/shriyays/Desktop/chromedriver-mac-arm64/chromedriver"

os.environ['PATH'] += r"/Users/shriyays/Desktop/chromedriver-mac-arm64/chromedriver" #code level configuration of environment variable path
#r(raw string) - used as a prefix to strings when you want blackslash to be treated as a literal

driver = webdriver.Chrome(driver_path)

driver.get("https://www.olx.in/")
driver.implicitly_wait(5) #waits for 5 seconds or until before the page loads or the task is done
#implicitly_wait() - it is applied across all elements so it can be mentioned only once in the program 

driver.
my_element = driver.find_element(By.ID, "searchBox")
my_element.click()

e1=driver.find_element(By.CLASS_NAME,"")
e2=driver.find_element(By.NAME,"")
e3=driver.find_element(By.XPATH,"")

#explicit wait until some condition has been satified
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        e1,"text"
    )
)

