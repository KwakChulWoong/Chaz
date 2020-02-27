import sys
import io
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

firefox_option=Options()
firefox_option.add_argument("--headless") #CLI

driver=webdriver.Firefox(firefox_options=firefox_option,executable_path='D:/atom_py/section3/firefox/geckodriver')
driver.set_window_size(1920,1080)

driver.get('https://naver.com')
driver.save_screenshot("D:/atom_py/section3/firefox/website3.png")
driver.quit()

print('찰칵')
