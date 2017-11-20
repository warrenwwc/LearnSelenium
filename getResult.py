# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import json

startups = []
results = []

fo = open('startups.txt', 'r') 
for line in fo:
	startups.append(line)
fo.close()

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
#driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.maximize_window()

for startup in startups:
	try:
		dic = {}
		driver.get(startup)
		soup = BeautifulSoup(driver.page_source, "html.parser")
		dic['CompanyName'] = soup.select('.s-vgBottom0_5')[0].text;
		dic['Desc'] = soup.select('p')[0].text
		tags = ""
		for tag in soup.select('.tag'):
			tags += tag.text + " "
		dic['Tags'] = tags
		dic['CompanySize'] = soup.select('.js-company_size')[0].text
		dic['Url'] = soup.select('.company_url')[0].text
		results.append(dic)
	except IndexError:
		break

print json.dumps(results, indent = 4)
fo = open("results.txt", "w")
fo.write(json.dumps(results, indent = 4))
fo.close()
driver.quit()
print "Done"
