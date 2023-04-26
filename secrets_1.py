import time
import os
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import os

load_dotenv()

IBM_MAIL = os.environ.get('IBM_MAIL')
IBM_PASSWORD = os.environ.get('IBM_PASSWORD')


class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
    
    def login(self):
    
        driver =self.driver
        authenticationUser = driver.find_element(By.XPATH,"//*[@id='username']")
        time.sleep(1)
        authenticationUser.send_keys("ipalusercm@sg.ibm.com")
        time.sleep(3)
        sendUser = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[2]/div/div/div[1]/div/div/form/div[2]/div/div/button")
        print("user OK")
        sendUser.click(); 
        time.sleep(10)
        authenticationPass = driver.find_element(By.XPATH,"//*[@id='password']")
        time.sleep(1)
        authenticationPass.send_keys("OscwiUserlogin@7890")
        time.sleep(5)
        sendPass = driver.find_element(By.XPATH,"//*[@id='signinbutton']")
        sendPass.click(); 
        print("password OK")
        time.sleep(70)
        

        print("Holaaaaaa!!!!!!")
        # driver =self.driver
        
        # authentication = driver.find_element(By.XPATH,"//*[@id='credsDiv']")
        # authentication.click()
        # time.sleep(5)
     
        # authenticationE = driver.find_element(By.XPATH,"//*[@id='user-name-input']")
        # time.sleep(1)
        # authenticationE.send_keys(IBM_MAIL, Keys.ARROW_DOWN)
        # time.sleep(1)
        # authenticationP = driver.find_element(By.XPATH,"//*[@id='password-input']")
        # time.sleep(1)
        # authenticationP.send_keys(IBM_PASSWORD, Keys.ARROW_DOWN)
        # time.sleep(1)
        # login = driver.find_element(By.XPATH,"//*[@id='login-button']")
        # print("login OK")
        # login.click(); 


