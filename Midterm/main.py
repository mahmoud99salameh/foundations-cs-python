from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

def clean_browser():
      option= webdriver.ChromeOptions()
      option.add_argument('--incognito')
      driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                            options=option)
      return driver

if __name__ == '__main__':
      print('1')
      driver = clean_browser()
      print('2')
      driver.get('www.google.com')
