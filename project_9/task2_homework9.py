from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

dr = webdriver.Chrome()

dr.get('https://blog.skillfactory.ru/')
dr.find_element(By.CLASS_NAME, 'header-search').click()
dr.find_element(By.CLASS_NAME, 'search-field').send_keys('test')
dr.find_element(By.TAG_NAME, 'button').click()
wait = WebDriverWait(dr, 3, poll_frequency=0.1)
dr.find_element(By.CSS_SELECTOR, 'a.page-numbers').click()
dr.find_element(By.PARTIAL_LINK_TEXT, 'SQL').click()
dr.find_element(By.XPATH, '//*[@id="post-1466"]/div[4]/div[1]/div[2]/ol/li[3]/a').click()
dr.find_element(By.XPATH, '//*[@id="menu-item-2215"]/a').click()
dr.close()
