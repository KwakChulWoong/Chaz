import sys
import io
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

chrome_options=Options()
# chrome_options.add_argument("--headless") #창이 안뜨게

driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=r'D:/atom_py/section3/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://www.wishket.com/accounts/login/')
