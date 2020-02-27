import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

chrome_options=Options()

driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=r'D:/atom_py/section3/chrome/chromedriver')
driver.set_window_size(1920,1080)
driver.get('http://www.encar.com/dc/dc_carsearchlist.do?carType=kor&searchType=model&TG.R=A#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.Manufacturer.%ED%98%84%EB%8C%80.))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="stepModel"]/dl[1]/dd[6]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="sr_normal"]/tr[4]/td[1]/div/a/span/span').click()
