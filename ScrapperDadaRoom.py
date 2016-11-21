# -*- coding: utf-8 -*-

import dryscrape
from bs4 import BeautifulSoup
import time
import xlwt
import sys

def getNumVisits(ad):
	try:
		session = dryscrape.Session()
		session.visit(ad)
		response = session.body()
		soup = BeautifulSoup(response, 'lxml')
		labelHot = soup.find_all('div', attrs={'class': 'label-hot'})
		people = labelHot[1].find_all('span', attrs={'class': 'label'})
		return [people[0].text, time.strftime("%Y-%m-%d %H:%M:%S")]
	except:
		return ['0', time.strftime("%Y-%m-%d %H:%M:%S")]



if 'linux' in sys.platform:
    # start xvfb in case no X is running. Make sure xvfb 
    # is installed, otherwise this won't work!
    dryscrape.start_xvfb()

ad1 = 'http://www.dadaroom.com/mx/CuartoEn/Calle+Versalles+65,+Ju%C3%A1rez,+Mexico+City,+Mexico/293868'
ad2 = 'http://www.dadaroom.com/mx/CuartoEn/Calle+Versalles+72,+Ju%C3%A1rez,+Mexico+City,+Mexico/293856'
ad3 = 'http://www.dadaroom.com/mx/CuartoEn/Calle+Lisboa+47,+Ju%C3%A1rez,+Mexico+City,+Mexico/293908'

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Juarez Good looking")
sheet2 = book.add_sheet("Juarez Average looking")
sheet3 = book.add_sheet("Juarez Baseline")

sheet1.write(0, 0, "Date")
sheet1.write(0, 1, "Watching")
sheet2.write(0, 0, "Date")
sheet2.write(0, 1, "Watching")
sheet3.write(0, 0, "Date")
sheet3.write(0, 1, "Watching")

row = 1


while True:
	logFile = open('Experiment2-'+sys.argv[1]+'.log', 'a')
	message = "Getting views " + str(row) + " " + time.strftime("%Y-%m-%d %H:%M:%S") + '\n'
	logFile.write(message)

	[visits, date] = getNumVisits(ad1)
	sheet1.write(row, 0, date)
	sheet1.write(row, 1, visits)

	[visits, date] = getNumVisits(ad2)
	sheet2.write(row, 0, date)
	sheet2.write(row, 1, visits)

	[visits, date] = getNumVisits(ad3)
	sheet3.write(row, 0, date)
	sheet3.write(row, 1, visits)

	book.save("Experiment2-"+sys.argv[1]+".xls")
	logFile.close()

	row += 1
	time.sleep(20)


