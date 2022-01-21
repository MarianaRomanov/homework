from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


dr = webdriver.Chrome()
dr.get('https://www.softaculous.com/softaculous/demos/Oxwall')
dr.implicitly_wait(5)
el_frame = dr.find_elements(By.TAG_NAME, 'iframe')[1]
dr.switch_to.frame(el_frame)
dr.find_element(By.CLASS_NAME, 'ow_signin_label').click()
dr.find_element(By.NAME, 'identity').send_keys('demo')
dr.find_element(By.NAME, 'password').send_keys('demo')
dr.find_element(By.NAME, 'submit').click()

try:
    WebDriverWait(dr, 5).until_not(EC.presence_of_element_located((By.CLASS_NAME, 'ow_signin_label')))
except TimeoutException:
    print('Login is not successful')
