# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://qzone.qq.com')
driver.switch_to_frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()
driver.find_element_by_id('u').send_keys('wzwmxd@qq.com')
driver.find_element_by_id('p').send_keys('4181456184xu')
driver.find_element_by_id('login_button').click()
driver.quit()
