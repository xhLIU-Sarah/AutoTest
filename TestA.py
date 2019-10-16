# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging#log:owner-level-result;root(own)
logging.basicConfig(level= logging.DEBUG,filename='selenium.log',filemode='w',format='%(name)s-%(levelname)s-%(message)s')
#level:debug ,log,warning,error
driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get("http://www.bing.com")
logging.debug('home page opened')
driver.maximize_window()
driver.save_screenshot('screenshot/home.png')#screenshot
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'sb_form_q')))
#WebDriverWait(driver,10).until(EC.element_to_be_clickable(By.ID,'sb_form_q')))

#driver.find_element_by_name('q').text('python')

driver.find_element_by_id('sb_form_q').send_keys('python')
driver.find_element_by_id('sb_form_q').send_keys(Keys.ENTER)
#driver.find_element_by_id('sb_form_go').click()
assert driver.title.__contains__('python')
#assert 'python' in driver.title #same with contains
#time.sleep(3)
driver.quit()
#driver.close()# more windows tab close
