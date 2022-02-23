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

    # options.add_argument(r"user-data-dir=C:\\Users\\" + "mtl91125" + "\\AppData\\Local\\Microsoft\\Edge\\User Data".format(getpass.getuser()))

    PATH_ = 'C:\PATH\edgedriver_win64\msedgedriver.exe'
    driver = webdriver.Edge(PATH_)
    # driver = webdriver.Chrome(executable_path='C:\PATH\chromedriver.exe')
    return driver


def runTime():

    #facebook
    fbDv = setup()
    url = "https://www.facebook.com/OutdoorRangsit/posts/4926771320932770"

    newUrl = url.replace("www","m")
    fbDv.get(newUrl)
    waitFb = WebDriverWait(fbDv, 20, poll_frequency=1, ignored_exceptions=[
                                 ElementNotVisibleException, ElementNotSelectableException])

    waitFb.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mobile_login_bar']/div[2]/div/a[2]"))).click()
    waitFb.until(EC.element_to_be_clickable((By.ID,"m_login_email"))).send_keys("0953174393")
    waitFb.until(EC.element_to_be_clickable((By.ID,"m_login_password"))).send_keys("s.somphot")
    waitFb.until(EC.element_to_be_clickable((By.ID,"login_password_step_element"))).click()
    waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")
    
    # waitFb.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='facebook']/body"))).click()
    # waitFb.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='mount_0_0_/B']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div[4]/div/div/div[2]/div[3]/div[2]/form/div"))).click()

    #timeanddate
    driver = setup()
    driver = driver
    driver.get("https://www.timeanddate.com/")
    driver_g = driver


    wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[
                                 ElementNotVisibleException, ElementNotSelectableException])
    

    while True:
        hm = wait.until(EC.element_to_be_clickable((By.ID, "clk_hm")))
        sc = wait.until(EC.element_to_be_clickable((By.ID, "ij0")))
        hmText = [hm.text]
        scText = [sc.text]
                # print(hmText)
        # arr_sec = ["00","01","02","03","04","05","06","07","08","09"]
        # for i in len(arr_sec):

        hmInput = '19:00'

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['00']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")
        
        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['01']"):
                
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['02']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['03']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")
        
        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['04']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['05']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['06']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['07']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['08']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        if (str(hmText) == "['" + hmInput + "']"):
            i = 0
            if (str(scText) == "['09']"):
                waitFb.until(EC.element_to_be_clickable((By.NAME, "submit"))).click()
                waitFb.until(EC.element_to_be_clickable((By.ID, "composerInput"))).send_keys("รับ")

        else:
            print(str(hmText) + ":" + str(scText))
        


runTime()
