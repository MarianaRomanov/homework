from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidArgumentException

dr = webdriver.Chrome()
dr.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/#Button_Test_Cases')

# alert close
dr.find_element(By.NAME, 'B1').click()
dr.switch_to.alert.accept()

dr.find_element(By.NAME, 'submit').click()
dr.find_element(By.ID, 'primary-button').click()

# input + reset
dr.find_element(By.NAME, 'test').send_keys('test')
dr.find_element(By.NAME, 'reset').click()

# file upload
file_button = dr.find_element(By.NAME, 'B5')
try:
    file_button.send_keys("D://New.txt")
except InvalidArgumentException:
    print('No file')

# check if disabled
dis_button = dr.find_element(By.NAME, 'button2')
if dis_button.get_attribute('disabled'):
    print('Element is disabled')

# switch to new window
dr.find_element(By.PARTIAL_LINK_TEXT, 'mozilla').send_keys(Keys.LEFT_CONTROL, Keys.ENTER)
dr.switch_to.window(dr.window_handles[1])
dr.close()
dr.switch_to.window(dr.window_handles[0])
