from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.get("https://novaposhta.ua/")
dr.implicitly_wait(5)
menu = dr.find_element(By.XPATH, '//*[@id="top_menu"]/li[4]')
submenu = menu.find_elements(By.TAG_NAME, 'li')[0]
action = ActionChains(dr)
action.move_to_element(menu).pause(3)
action.click(submenu)
action.perform()
