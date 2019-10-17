from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
def Is_Elemnt_Exist(context,element):
    flag = True
    try:
        context.driver.find_element_by_css_selector(element)
        return flag
    except:
        flag = False
        return flag
def Web_Wait(context,id):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))