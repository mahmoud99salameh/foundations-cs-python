import webbrowser
import os
from selenium import webdriver
import time

browser = webdriver.Safari()
#open normal tab
def OpenNewTab():
    webbrowser.open('https://google.com', new=2)
#close tab
def CloseSafari():
        os.system('TASKKILL /F /IM safari.???')
#open tab with web driver
def OpenWithWebDriver():
      browser.get("https://google.com")
      
def CloseTab():
      browser.close()




