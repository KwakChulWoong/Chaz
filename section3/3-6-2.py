import sys
import io
from selenium import webdriver
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

driver=webdriver.Chrome('D:/atom_py/section3/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('https://google.com')
time.sleep(3)
driver.save_screenshot("D:/atom_py/section3/chrome/website1.png")

driver.get('https://daum.net')
time.sleep(3)
driver.save_screenshot("D:/atom_py/section3/chrome/website2.png")
driver.quit()

print("스크린 샷!")
