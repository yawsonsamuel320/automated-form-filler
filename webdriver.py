from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://forms.gle/zJpVE1ck4rxXbWFa7")

# Wait for one second, until page gets fully loaded
time.sleep(1)

inputs = {
    "First Name": "Samuel",
    "Last Name": "Yawson",
    "Phone": 1,
}
for input_name in inputs:
    text_input = driver.find_element(By.XPATH, f"//div[contains(@jsmodel, 'CP1oW') and contains(., '{input_name}')]//input[@type='text']")
    text_input.send_keys(inputs[input_name])
    time.sleep(2)

driver.close()