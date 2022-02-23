import imp
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException,  ElementNotSelectableException, ElementNotVisibleException
# from tenacity import time
import pandas as pd
import os

def setup():
    PATH_ = 'C:\PATH\edgedriver_win64\msedgedriver.exe' # Call path web-driver
    driver = webdriver.Edge(PATH_)
    return driver

def runTime():

    #facebook
    fbDv = setup()
    url = "https://www.facebook.com/OutdoorRangsit/posts/4926771320932770" #Link post in Facebook 

    newUrl = url.replace("www","m")
    fbDv.get(newUrl)
    waitFb = WebDriverWait(fbDv, 20, poll_frequency=1, ignored_exceptions=[
                                 ElementNotVisibleException, ElementNotSelectableException])

    waitFb.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mobile_login_bar']/div[2]/div/a[2]"))).click()
    waitFb.until(EC.element_to_be_clickable((By.ID,"m_login_email"))).send_keys("Your Email") #Input your email for login facebook
    waitFb.until(EC.element_to_be_clickable((By.ID,"m_login_password"))).send_keys("You Pass") #Input your passwork for login facebook
    waitFb.until(EC.element_to_be_clickable((By.ID,"login_password_step_element"))).click()
    waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("Data") #Input data 

    #time-and-date from web timeanddate have neary time in facebook
    driver = setup()
    driver = driver
    driver.get("https://www.timeanddate.com/")


    wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
                                 ElementNotVisibleException, ElementNotSelectableException])
    

    while True:
        hm = wait.until(EC.element_to_be_clickable((By.ID, "clk_hm")))
        sc = wait.until(EC.element_to_be_clickable((By.ID, "ij0")))
        hmText = [hm.text] #Get HH:mm from https://www.timeanddate.com/
        scText = [sc.text] #Get sec from https://www.timeanddate.com/

        hmStart = '19:00' #Start time
        hmStop = '20:00' #Stop time

        if (str(hmText) == "['" + hmStart + "']"):
            if (str(scText) == "['00']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("data")
         
        if (str(hmText) == "['" + hmStop + "']"):
            break
        
        else:
            print(str(hmText) + ":" + str(scText))

runTime()
