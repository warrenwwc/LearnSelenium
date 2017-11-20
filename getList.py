# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from bs4 import BeautifulSoup
import pickle

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
#driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.maximize_window()

markets = ['E-Commerce', 'Education', 'Enterprise+Software', 'Games', 'Healthcare']

links = []

fo = open("startups.txt", "w")

for market in markets:
	driver.get("https://angel.co/companies?locations[]=1644-Hong+Kong&company_types[]=Startup&markets[]=" + market)
	while True:
		try:
			element = WebDriverWait(driver, 5).until(
				EC.presence_of_element_located((By.CSS_SELECTOR, ".more"))
			)
			driver.find_element_by_css_selector('.more').click()
		except (NoSuchElementException, TimeoutException, StaleElementReferenceException):
			print market
			break
	soup = BeautifulSoup(driver.page_source, "html.parser")
	for i in soup.select('.dc59.frw44 .startup .company .name a'):
		print i['href']
		#links += i['href']
		fo.write(i['href'] + "\n")
		
fo.close()
driver.quit()
print "Done"
