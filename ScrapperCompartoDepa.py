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

def extractProfileInfo(profile):
	href = profile.find_element_by_class_name('listing__link').get_attribute("href")
	headline = profile.find_element_by_class_name("listing-meta__headline").text.split("-")
	name = headline[0]
	age = headline[1]
	#Some profiles don't have occupation, this if handles it
	if len(headline) >=3 :
		ocuppation = headline[2]
	else:
		ocuppation = "No especifica"
	freshness = profile.find_element_by_class_name("ui-text--orange").text
	budget = profile.find_element_by_class_name("listing-meta__price--prefix").text
	movingDate = profile.find_element_by_xpath("//span[@data-bind='text: resultItem.MovingDateForDisplay']").text
	return href, name, age, ocuppation, budget, movingDate, freshness


PROFILES_PER_PAGE = 20

#Initialize excel sheet
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Data 1")
#href, name, age, ocuppation, budget, movingDate, freshness
sheet1.write(0, 0, "link")
sheet1.write(0, 1, "name")
sheet1.write(0, 2, "age")
sheet1.write(0, 3, "ocuppation")
sheet1.write(0, 4, "budget")
sheet1.write(0, 5, "movingDate")
sheet1.write(0, 6, "freshness")

URL = 'http://www.compartodepa.com.mx/search/profiles/H1612160264747?amin=18&amax=99&gen=0&occ=0&pic=0&srt=3&rad=2000&lat=19.359167098999&lng=-99.2704620361328'

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

	profiles = driver.find_elements_by_class_name("listing__row")
	for profile in profiles:
		[href, name, age, ocuppation, budget, movingDate, freshness] = extractProfileInfo(profile)
		sheet1.write(rowCounter, 0, href)
		sheet1.write(rowCounter, 1, name)
		sheet1.write(rowCounter, 2, age)
		sheet1.write(rowCounter, 3, ocuppation)
		sheet1.write(rowCounter, 4, budget)
		sheet1.write(rowCounter, 5, movingDate)
		sheet1.write(rowCounter, 6, freshness)
		rowCounter = rowCounter + 1
		book.save("Report-SantaFe"+".xls")

	pageCounter = pageCounter + 1

print 'Scrapping finished'

#Closes the current window
driver.close()

