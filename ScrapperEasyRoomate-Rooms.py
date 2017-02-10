#Install selenium via pip
#	pip install selenium
#Install NodeJS
#install phantomjs via Nodejs 
#	npm -g install phantomjs
#Check phantmjs exec path:
# 	/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs

#http://www.compartodepa.com.mx/search/profiles/H161215225422750?lat=19.4298610687256&lng=-99.1676177978516&amin=18&amax=99&gen=0&occ=0&pic=0
#http://www.compartodepa.com.mx/search/profiles/H161215225422750?lat=19.4298610687256&lng=-99.1676177978516&amin=18&amax=99&gen=0&occ=0&pic=0

from selenium import webdriver
import time
import xlwt
import sys

def getNumPages(driver, URL):
	print 'Calculating number of pages to scrap'
	driver.get(URL) 
	time.sleep(5)
	resultsCountText = driver.find_element_by_class_name("results-count--dynamic").text.split(' ')[0]
	resultsCount = int(resultsCountText.replace(',', ''))
	return resultsCount/PROFILES_PER_PAGE + 1

def extractRoomInfo(profile):
	href = profile.find_element_by_class_name('listing__link').get_attribute("href")
	headline = profile.find_element_by_class_name("listing-meta__headline").text.split("-")
	price = profile.find_element_by_class_name("listing-img__price").find_element_by_tag_name('span').text
	freshness = profile.find_element_by_class_name("ui-text--orange").text
	metaProfile = profile.find_element_by_class_name("listing-meta__profile")
	availableDate = metaProfile.find_element_by_xpath("//li[3]/span").text
	housemates = metaProfile.find_element_by_xpath("//li[4]/span").text
	description = profile.find_element_by_class_name("listing-meta__desc").find_element_by_tag_name('h2').text
	return href, headline, price, freshness, availableDate, housemates, description


URL = 'http://www.easyroommate.com/search/rooms/L17020916384596?rmax=9999&bed=1&pic=0&doub=0&furn=0&shor=0&amin=18&amax=99&srt=3&rad=2000&lat=37.7785189&lng=-122.4056395'
reportName = 'I33'

PROFILES_PER_PAGE = 20

#Initialize excel sheet
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Data 1")
sheet1.write(0, 0, "link")
sheet1.write(0, 1, "headline")
sheet1.write(0, 2, "price")
sheet1.write(0, 3, "freshness")
sheet1.write(0, 4, "availableDate")
sheet1.write(0, 5, "housemates")
sheet1.write(0, 6, "description")

driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
numPages = getNumPages(driver, URL)
print 'Number of pages to scrap: ', numPages

#for the pagination
pageCounter = 1
#for the excel sheet
rowCounter = 1
while pageCounter <= numPages:

	print 'Scrapping page number', pageCounter, 'out of ', numPages
	driver.get(URL+'&pag='+str(pageCounter)) 
	time.sleep(5)

	rooms = driver.find_elements_by_class_name("listing__row")
	for room in rooms:
		href, headline, price, freshness, availableDate, housemates, description = extractRoomInfo(room)
		sheet1.write(rowCounter, 0, href)
		sheet1.write(rowCounter, 1, headline)
		sheet1.write(rowCounter, 2, price)
		sheet1.write(rowCounter, 3, freshness)
		sheet1.write(rowCounter, 4, availableDate)
		sheet1.write(rowCounter, 5, housemates)
		sheet1.write(rowCounter, 6, description)
		rowCounter = rowCounter + 1
		book.save(reportName+".xls")

	pageCounter = pageCounter + 1

print 'Scrapping finished'

#Closes the current window
driver.close()

