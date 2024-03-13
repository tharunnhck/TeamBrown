from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

import random




print("opening...")
driver = webdriver.Chrome()
driver.get("https://twitter.com/")
driver.maximize_window()
time.sleep(2)


@allure.severity(allure.severity_level.MINOR)
def test_login():
    signinicon = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
    signinicon.click()

    time.sleep(2)
    username = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]')

    username.click()
    time.sleep(2)
    username2 = driver.find_element(By.NAME, 'text')
    username2.send_keys("teambrown2003")
        # username.submit()
        # time.sleep(1)
    nextbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    nextbutton.click()
    time.sleep(1)
    passwordbutton = driver.find_element(By.NAME, 'password')

    time.sleep(2)
    passwordbutton.send_keys("cocomelon12")
    loginbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    loginbutton.click()
    time.sleep(5)



def test_tweet():
    whatshappening = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/a/div[2]/div/div')
    whatshappening.click()

    time.sleep(1)
    postbar = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    list1 = [range(10, 1000)]
    randomm = random.choice(list1)

    postbar.send_keys("Wassssuppppp???")

    time.sleep(1)
    postbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div')
    postbutton.click()
    time.sleep(5)


def test_search():

    searchbutton = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div')
    searchbutton.click()
    time.sleep(10)
    searchbutton1 = driver.find_element(By.NAME,'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]')
    searchbutton1.send_keys("Maggi")
    searchbutton1.submit()
    time.sleep(10)


def test_logout():
    time.sleep(2)
    accountsbutton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/div[4]/div')
    accountsbutton.click()
    logoutbutton = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]')
    logoutbutton.click()
    logoutbutton2 = driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div')
    logoutbutton2.click()
    time.sleep(1)


