from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys
import json
from datetime import datetime as dt
import time

try:
    
    with open("config.json", 'r') as config:

        config = json.load(config)
        if not {"email", "password"}.issubset(set(config.keys())):
            raise Exception()
            
        email = config["email"]
        pwd = config["password"]
    
except:
    
    print(
        "Please create a valid config file in order to log in.\n" +
        "Exiting..."
    )
    
    sys.exit(1)

while True:
    
    # run the following cell at a given time
    if dt.now().hour == <hour> and dt.now().minute == <minute> and dt.now().second == <second>: break
    else: time.sleep(0.5)

options = webdriver.ChromeOptions()
options.headless = True
evnt_url = ""
state = 1 # conditional state
sleep_time = 2
sleep_time_ini = 2 # initial sleep time 

while state:
    
    driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    driver.get("https://meetup.com/login/")
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "current-password").send_keys(pwd)
    button = driver.find_element(By.NAME, "submitButton")
    driver.execute_script("arguments[0].click();", button)
    
    time.sleep(sleep_time_ini)
    
    if sleep_time == sleep_time_ini: print("Login successful ...")
    
    
    try:
        driver.get(evnt_url)
        time.sleep(2)
        button = driver.find_element(By.CSS_SELECTOR, ".leading-8.text-white.font-semibold.whitespace-nowrap")
        # driver.find_element(By.XPATH, '//button[text()="Attend online"]').click()
        driver.execute_script("arguments[0].click();", button)
        
        
        # now we handle a potential modal
        
        """
        try:
            time.sleep(1)
            button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
            # button = driver.find_element(By.CSS_SELECTOR, "div[class='flex-grow self-end']").click()
            driver.execute_script("arguments[0].click();", button)
            
        except NoSuchElementException:
            print("No modal pops up this time")
        """
    
    except NoSuchElementException:
        sleep_time_ini += 1
        
    else:
        state = 0
        hour = dt.now().hour
        minute = dt.now().minute
        sec = dt.now().second
        print(f"Your attendance has been confirmed at {hour}:{minute}:{sec}!")
