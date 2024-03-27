from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import requests

class WebAutomation:
    chrome_options = Options()
    
    def __init__(self, console = False):
        if console == True:
            self.chrome_options.add_argument("--headless=new")
        else:
            pass
    
        self.driver = webdriver.Chrome(options = self.chrome_options)

    def start(self):
        return(self.driver)

    def quit(self):
        self.driver.quit()

class AadharVerification:
    target_url = 'https://myaadhaar.uidai.gov.in/check-aadhaar-validity'

    def __init__(self, driver):
        self.driver = driver
        driver.get(self.target_url)
    
    def getCaptcha(self):
        driver = self.driver
        
        WebDriverWait(driver, 900).until(
            EC.presence_of_element_located((By.CLASS_NAME, "auth-form__captcha-image"))
        )

        while self.driver.execute_script("return(document.querySelector('.auth-form__captcha-image').outerHTML)") == '<img class="auth-form__captcha-image check-aadhaar-validity__captcha-image" alt="captcha">':
            pass

        captcha = self.driver.execute_script("return(document.querySelector('.auth-form__captcha-image').outerHTML)")
        return({'status':'success','captcha':captcha})

    def inputDetails(self,uid,captcha):
        driver = self.driver

        UID_input = driver.find_elements(By.CLASS_NAME, "sc-fBWQRz")[0]
        UID_input.send_keys(uid)
        
        captcha_input = driver.find_elements(By.CLASS_NAME, "sc-fBWQRz")[1]
        captcha_input.send_keys(captcha)
        return({'status':'success'})

    def submit(self):
        driver = self.driver
        driver.execute_script("document.querySelector('.button_btn__HeAxz').click()")
        return({'status':'success'})

    def fetchResponse(self):
        driver = self.driver
        
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "check-aadhaar-validity-response__card"))
        )

        response = driver.execute_script("return(document.querySelector('.check-aadhaar-validity-response__card').innerText)")
        return({'status':'success','response':response})

class IFSC_Verification:
    target_url = 'https://ifsc.bankifsccode.com/'

    def __init__(self, driver):
        self.driver = driver
        driver.get(self.target_url)


    def inputDetails(self,ifsc):
        driver = self.driver

        IFSC_input = driver.find_element(By.ID, "ifsccode")
        IFSC_input.send_keys(ifsc)

        return({'status':'success'})

    def submit(self):
        driver = self.driver
        driver.find_element(By.NAME, "submit").click()
        return({'status':'success'})

    def fetchResponse(self):
        driver = self.driver
        
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/table[1]/tbody/tr[9]/td[2]/table/tbody/tr/td[1]/div/div"))
        )

        response = driver.execute_script("return(document.querySelectorAll('.text6')[1].innerText)")
        return({'status':'success','response':response})
