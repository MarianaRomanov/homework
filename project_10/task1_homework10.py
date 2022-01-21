from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
dr.get('https://www-archive.mozilla.org/projects/ui/accessibility/unix/testcase/html/')
# checkbox check
check_box = {dr.find_element(By.ID, 'checkbox1'), dr.find_element(By.ID, 'checkbox2')}
[i.click() for i in check_box if not i.is_selected()]

# radio check
radio_A = dr.find_element(By.XPATH, '//*[@id="mainContent"]/form[2]/p[1]').find_elements(By.NAME, 'A')
[i.send_keys(Keys.ARROW_UP) for i in radio_A if i.is_selected()]

radio_B = dr.find_element(By.XPATH, '//*[@id="mainContent"]/form[2]/p[2]').find_elements(By.NAME, 'B')
[i.click() for i in radio_B if not i.is_selected()]

radio_C = dr.find_element(By.TAG_NAME, 'fieldset').find_elements(By.NAME, 'C')
[i.send_keys(Keys.ARROW_DOWN) for i in radio_C if not i.is_selected()]

[print(i.get_attribute('value')) for i in radio_A+radio_B+radio_C]

# drop-down list + select
list_1 = Select(dr.find_element(By.ID, 'components'))
list_1.select_by_index(2)
list_1.select_by_value('MAI')

list_2 = Select(dr.find_element(By.ID, 'city'))
v = 5, 15, 18
[list_2.select_by_value(str(i)) for i in v]
list_2.select_by_visible_text('Haikou')
[list_2.select_by_index(i) for i in range(10) if i % 2 == 0]

list_3 = dr.find_element(By.ID, 'flavor').find_elements(By.TAG_NAME, 'option')
[print(f'Element "{i.text}" is disabled') for i in list_3 if not i.is_enabled()]

list_4 = Select(dr.find_element(By.NAME, 'Select list'))
list_4.select_by_index(3)

list_5 = dr.find_element(By.NAME, 'op_sys').find_elements(By.TAG_NAME, 'option')
[print(f'Element "{i.text}" is selected') for i in list_5 if i.is_selected()]

list_6 = dr.find_element(By.ID, 'onedisabled').find_elements(By.TAG_NAME, 'option')
[print(f'Element "{i.text}" is disabled') for i in list_6 if not i.is_enabled()]
