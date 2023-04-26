import unittest
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from secrets_1 import LoginPage
from selenium.webdriver.support.ui import Select

import os
from slack_connection import slack
from flags import *


IBM_MAIL = os.environ.get('IBM_MAIL')
CHROME_DRIVER = os.environ.get('CHROME_DRIVER')
LOG_FILE_PATH = os.environ.get('LOG_FILE_PATH')

class using_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   

    def test_00(self): 
        MessagePassed = "Test 01 LogIn is: Correct :adhoc-ontrack:"
        MessageUnpassed = "Test 01 LogIn is : Fail :adhoc-blocked:"
        
        try:

            header_json()
            driver = self.driver
            driver.get("https://www-40preprod.cpc.ibm.com/procurement/osc/index.wss") 
            time.sleep(10)
            print('Test Access login  ')
            LoginP = LoginPage(driver)
            LoginP.login()
            time.sleep(10)

            signIn = driver.find_element(By.XPATH,"//*[@id='ibm-content-main']/div/div[2]/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td/p/a")
            signIn.click(); 
            print('login is correct')
            survieb=driver.find_element(By.XPATH,"//*[@id='ibm-content-main']/div/div[2]/div[3]/p/a") 
            survieb.click()
            time.sleep(5)
            print("New order ,  Pasoo")

            compName=driver.find_element(By.XPATH,"//*[@id='cmpo']") 
            compName.send_keys("OSCWI27MAR23") 
            print("CM PO")
            time.sleep(5) 


           
            select=driver.find_element(By.XPATH,"//*[@id=shipTo']")
            opcion=select.find_elements(By.TAG_NAME,"option")
            time.sleep(3)
            for option in opcion:
                print("Los valores son: %s" % option.get_attribute("value"))
                option.click()
                time.sleep(1)
            seleccionar = Select(driver.find_element(By.XPATH,"//*[@id=shipTo']"))
            seleccionar.select_by_value("0015101013")
            time.sleep(5)
            # select = select.select_by_visible_text('Science-Based Industrial Park,Hsinchu 300, Taiwan,128477,128477,SG')
            # #Checkbox
            # survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
            # survieb.click()
            # time.sleep(5)
            
           

            passed(MessagePassed)
            # slack()
        except:
            print("NO Pasoo")
            unpassed(MessageUnpassed)
            # slack()


    def test_01(self): 
        MessagePassed = "Test 01 LogIn is: Correct :adhoc-ontrack:"
        MessageUnpassed = "Test 01 LogIn is : Fail :adhoc-blocked:"
        
        try:

            header_json()
            driver = self.driver
            driver.get("https://www-40preprod.cpc.ibm.com/procurement/osc/index.wss") 
            time.sleep(10)
            print('Test Access login  ')
            LoginP = LoginPage(driver)
            LoginP.login()
            time.sleep(10)

            signIn = driver.find_element(By.XPATH,"//*[@id='ibm-content-main']/div/div[2]/table/tbody/tr[2]/td[1]/table/tbody/tr[5]/td/p/a")
            signIn.click(); 
            print('login is correct')
            survieb=driver.find_element(By.XPATH,"//*[@id='ibm-content-main']/div/div[2]/div[3]/p/a") 
            survieb.click()
            time.sleep(5)
            print("New order ,  Pasoo")

            compName=driver.find_element(By.XPATH,"//*[@id='cmpo']") 
            compName.send_keys("OSCWI27MAR23") 
            print("CM PO")
            time.sleep(5) 

            
            select=driver.find_element(By.XPATH,"//*[@id=shipTo']")
            opcion=select.find_elements(By.TAG_NAME,"option")
            time.sleep(3)
            for option in opcion:
                print("Los valores son: %s" % option.get_attribute("value"))
                option.click()
                time.sleep(1)
            seleccionar = Select(driver.find_element(By.XPATH,"//*[@id=shipTo']"))
            seleccionar.select_by_value("0015101005")
            time.sleep(5)
            # shippingAddress=driver.find_elements(By.XPATH,"//*[@id='shipTo']")
            # shippingAddress.click()
            # WorklistButton=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/aside/nav/ul/li[2]")
            # WorklistButton.click
            # print('Search Button is correct')

            # searchBu=driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/aside/nav/ul/li[1]") 
            # searchBu.click()
            # time.sleep(5) 
            print('Test Correct')


            passed(MessagePassed)
            # slack()
        except:
            unpassed(MessageUnpassed)
            # slack()
            print('no paso')
            

    # def test_102(self): 
    #     MessagePassed = "Test 102 Search without result is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 102 Search without result is: Fail :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 102 Default search without result')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')
    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(5) 
            
    #         empyInvoice=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[2]/div/div[2]/table/tr") 
    #         empyInvoice.click()
    #         print('Default search without result OK')
    #         time.sleep(5) 

    #         passed(MessagePassed)
         
    #     except:
    #         unpassed(MessageUnpassed)
    

    # def test_103(self): 
    #     MessagePassed = "Test 103 Search field  is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 103 Search field  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 103 Search field ')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            
    #         vendorInvoiceR=driver.find_element(By.XPATH,"//*[@id='1']/td[6]")
    #         vendorInvoiceR.click()
    #         print('Vendor invoice number OK')
            

    #         passed(MessagePassed)
    #         # slack()
         
    #     except:
    #         unpassed(MessageUnpassed)
    #         # slack()

    # def test_104(self): 
    #     MessagePassed = "Test 104 Open invoice image is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 104 Open invoice image  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 104 Open invoice image')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            

    #         vendorInvoiceR=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div/div[2]/table/tbody/tr/td[2]")
    #         vendorInvoiceR.click()
    #         print('Vendor invoice number OK')
            
    #         passed(MessagePassed)
    #         # slack()
         
    #     except:
    #         unpassed(MessageUnpassed)
    #         # slack()
    
    # def test_105(self): 
    #     MessagePassed = "Test 105 Edit attributes is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 105 Edit attributes is: Fail :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 105 edit attributes')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            
    #         survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
    #         survieb.click()
    #         time.sleep(3)

    #         atributesB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[1]/button[1]") 
    #         atributesB.click()
    #         atributesB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[2]/section/div[2]/button") 
    #         atributesB.click()
    #         print('Atribute button OK')
    #         time.sleep(4)
            
    #         atributesC=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[2]/section/div[2]/button[3]") 
    #         atributesC.click()
    #         print('Atribute  Close button OK')
    #         time.sleep(6)

    #         atributesB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[1]/button[1]") 
    #         atributesB.click()
    #         atributesB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[2]/section/div[2]/button") 
    #         atributesB.click()
    #         time.sleep(4)

    #         poNumberEdit=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[2]/div/div/table/tbody/tr[6]/td[2]/span/div/div/div/input")
    #         poNumberEdit.clear()
    #         time.sleep(3)
    #         poNumberEdit.send_keys("47000061121") 
    #         time.sleep(5)
            
    #         saveB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[3]/div[2]/section/div[2]/button[2]") 
    #         saveB.click()
    #         time.sleep(4)

    #         passed(MessagePassed)
         
    #     except:
    #         unpassed(MessageUnpassed)
    
    # def test_106(self): 
    #     MessagePassed = "Test 106 Adding Notelog is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 106 Adding Notelog  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 106 Adding Notelog')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            

    #         survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
    #         survieb.click()
    #         time.sleep(3)

    #         noteLog=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[3]/div[1]/button[2]") 
    #         noteLog.click()
    #         time.sleep(3) 

    #         notLogT=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[3]/div[2]/div[2]/div[2]/textarea")
    #         notLogT.send_keys("Sanitytest note") 
    #         time.sleep(3) 

    #         notLogB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[3]/div[2]/div[3]/button")
    #         notLogB.click()
    #         time.sleep(3) 


    #         passed(MessagePassed)
    #         # slack()
         
    #     except:
    #         unpassed(MessageUnpassed)
    #         # slack()

    # def test_107(self): 
    #     MessagePassed = "Test 107 Viewing History tab is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 107 Viewing History tab  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 107 Viewing History tab')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            

    #         survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
    #         survieb.click()
    #         time.sleep(3)

    #         historyB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[3]/div[1]/button[3]") 
    #         historyB.click()
    #         time.sleep(3) 

    #         passed(MessagePassed)
    #         # slack()
         
    #     except:
    #         unpassed(MessageUnpassed)
    #          # slack()

    
    # def test_108(self): 
    #     MessagePassed = "Test 108 Downloading invoice is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 108 Downloading invoice  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 108 Downloading invoice ')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            

    #         survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
    #         survieb.click()
    #         time.sleep(3)

    
    #         downloadB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[2]/div/section/div/div[2]/button[3]") 
    #         downloadB.click()
    #         print('Download button OK')
    #         time.sleep(4)
    
    #         passed(MessagePassed)
    #         # slack()
         
    #     except:
    #         unpassed(MessageUnpassed)
    #         # slack()

    # def test_109(self): 
    #     MessagePassed = "Test 109 Routing invoice: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 109 Routing invoice  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 109 Routing invoice')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            

    #         survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
    #         survieb.click()
    #         time.sleep(3)

    #         routeB=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[2]/div/section/div/div[2]/button[2]") 
    #         routeB.click()
    #         time.sleep(4)

    #         routeDoc=driver.find_element(By.XPATH,"//*[@id='root']/div[3]/div[1]/div/div/div[2]/form/div[1]/button[1]") 
    #         routeDoc.click()
    #         time.sleep(4)
          
    #         passed(MessagePassed)
    #         # slack()
         
    #     except:
    #         unpassed(MessageUnpassed)
    #         # slack()

    # def test_110(self): 
    #     MessagePassed = "Test 110 Process invoice is: Correct :adhoc-ontrack:"
    #     MessageUnpassed = "Test 110 Process invoice  is: Fail  :adhoc-blocked:"
        
    #     try:    
    #         driver = self.driver
    #         driver.get("https://ap-invoices-frontend-test.dal1a.ciocloud.nonprod.intranet.ibm.com/finance/wwimage/workflow/invoices") 
    #         time.sleep(10)
    #         print('Test 110 Process invoice')
    #         LoginP = LoginPage(driver)
    #         LoginP.login()
    #         time.sleep(10)

    #         print('login is correct')

    #         vendorInvoiceN=driver.find_element(By.XPATH,"//*[@id='VendorInvNumber']")
    #         vendorInvoiceN.send_keys("IBMtestForSanity001") 

    #         searchB=driver.find_element(By.XPATH,"//*[@id='root']/main/div/div/div[1]/div/div[4]/button") 
    #         searchB.click()
    #         time.sleep(2) 
            

    #         survieb=driver.find_element(By.XPATH,"//*[@id='1']/td[1]/div/label") 
    #         survieb.click()
    #         time.sleep(3)

    #         process=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div[2]/div/section/div/div[2]/button[1]")
    #         process.click()
    #         print('Process Buttom')
    #         time.sleep(5)

    #         processDoc=driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/label[1]")
    #         processDoc.click()
    #         print('Process Document')
    #         time.sleep(3)

    #         processB=driver.find_element(By.XPATH," //*[@id='root']/div[3]/div[1]/div/div/div[3]/button[2]")
    #         processB.click()
    #         time.sleep(3)
    #         passed(MessagePassed)

    #         slack()
    #     except:
    #         unpassed(MessageUnpassed)
    #         slack()
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()
