#Install selenium via pip
#	pip install selenium
#Install NodeJS
#install phantomjs via Nodejs 
#	npm -g install phantomjs
#Check phantmjs exec path:
# 	/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs

#This version uses Chrome drive, which can be downloaded here:
#https://sites.google.com/a/chromium.org/chromedriver/getting-started

#This version divides de document in 4

from selenium import webdriver
import time
import xlwt
import sys

PROFILES_PER_PAGE = 30

#Change this for new report
URL = 'https://www.trulia.com/for_rent/Houston,TX/APARTMENT,APARTMENT_COMMUNITY,APARTMENT%7CCONDO%7CTOWNHOUSE,CONDO,COOP,LOFT,TIC_type/'
reportName = 'F13-2'

#for the pagination
pageCounter = 81
#numPages
numPages = 110
#for the excel sheet
rowCounter = 1

def extractProfileInfo(profile):
	href = profile.find_element_by_class_name('tileLink').get_attribute("href")
	price = profile.find_element_by_class_name("cardPrice").text
	details = profile.find_element_by_class_name('listInline').find_elements_by_tag_name('li')
	rooms = 'No data'
	baths = 'No data'
	area = 'No data'
	numAttributes = len(details)

	if numAttributes == 3 :
		rooms = details[0].text
		baths = details[1].text
		area = details[2].text
	elif numAttributes == 2:
		rooms = details[0].text
		baths = details[1].text
	elif numAttributes == 1:
		rooms = details[0].text

	address = profile.find_element_by_class_name('cardDetails').find_element_by_tag_name('p').text


	return href, price, rooms, baths, area, address


#Initialize excel sheet
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Data")
#href, name, age, ocuppation, budget, movingDate, freshness
sheet1.write(0, 0, "URL")
sheet1.write(0, 1, "Price")
sheet1.write(0, 2, "Num Rooms")
sheet1.write(0, 3, "Num Baths")
sheet1.write(0, 4, "Area")
sheet1.write(0, 5, "Location")

# driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
driver = webdriver.Chrome(executable_path='./chromedriver')

print 'Number of pages to scrap: ', numPages
while pageCounter <= numPages:

	print 'Scrapping page number', pageCounter, 'out of ', numPages
	driver.get(URL+ str(pageCounter) + '_p/') 
	time.sleep(3)

	profiles = driver.find_elements_by_class_name("cardContainer")
	for profile in profiles:
		[link, price, rooms, baths, area, address] = extractProfileInfo(profile)
		sheet1.write(rowCounter, 0, link)
		sheet1.write(rowCounter, 1, price)
		sheet1.write(rowCounter, 2, rooms)
		sheet1.write(rowCounter, 3, baths)
		sheet1.write(rowCounter, 4, area)
		sheet1.write(rowCounter, 5, address)
		rowCounter = rowCounter + 1
		#Change this for new document
		book.save(reportName+".xls")

	pageCounter = pageCounter + 1

print 'Scrapping finished'

#Closes the current window
driver.close()

