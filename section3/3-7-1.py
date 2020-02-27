import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding='utf-8')

class NcafeWriteAtt:
    # 초기화 실행(webdriver 설정)
    def __init__(self) :
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=r"D:/atom_py/section3/chrome/chromedriver")
        self.driver.implicitly_wait(5)

    def writeAttendCheck(self) :
        self.driver.get("https://cafe.naver.com/airmanwannabe")
        self.driver.find_element_by_xpath('//*[@id="gnb_login_button"]/span[3]').click()
        self.driver.implicitly_wait(1)
        self.copy_input('//*[@id="id"]','socratechnic')
        self.driver.implicitly_wait(1)
        self.copy_input('//*[@id="pw"]','cjfdndqjvm0401-')
        self.driver.find_element_by_xpath('//*[@id="log.login"]').click()
        self.driver.implicitly_wait(3)
        time.sleep(3)
        self.driver.find_element_by_name('//*[@id="menuLink10"]').click()
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id('cmtinput').send_keys('출석체크')
        self.driver.find_element_by_xpath('//*[@id="menuLink10"]').click()
        time.sleep(3)


    def copy_input(self,xpath,input):
            pyperclip.copy(input)
            self.driver.find_element_by_xpath(xpath).click()
            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
            time.sleep(3)

    # 소멸자 (생성자를 닫아주는 역활)
    # def __del__(self) :
    #     self.driver.quit()
    #
    #

ns = NcafeWriteAtt()
ns.writeAttendCheck()
