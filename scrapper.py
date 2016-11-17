import dryscrape
from bs4 import BeautifulSoup
import time
import xlwt

def getNumVisits(ad):
	session = dryscrape.Session()
	session.visit(ad)
	response = session.body()
	soup = BeautifulSoup(response, 'lxml')
	labelHot = soup.find_all('div', attrs={'class': 'label-hot'})
	people = labelHot[1].find_all('span', attrs={'class': 'label'})
	return [people[0].text, time.strftime("%Y-%m-%d %H:%M:%S")]



ad1 = 'http://www.dadaroom.com/mx/CuartoEn/Ju%C3%A1rez,+Mexico+City,+Cuauht%C3%A9moc,+Mexico/293901'
ad2 = 'http://www.dadaroom.com/mx/CuartoEn/Ju%C3%A1rez,+Mexico+City,+Cuauht%C3%A9moc,+Mexico/293908'
ad3 = 'http://www.dadaroom.com/mx/CuartoEn/Ju%C3%A1rez,+Mexico+City,+Cuauht%C3%A9moc,+Mexico/293897'

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("17Nov Juarez Good looking")
sheet2 = book.add_sheet("17Nov Juarez Average looking")
sheet3 = book.add_sheet("17Nov Juarez Baseline")

sheet1.write(0, 0, "Date")
sheet1.write(0, 1, "Watching")
sheet2.write(0, 0, "Date")
sheet2.write(0, 1, "Watching")
sheet3.write(0, 0, "Date")
sheet3.write(0, 1, "Watching")

row = 1

while True:
	print "Getting views"

	[visits, date] = getNumVisits(ad1)
	sheet1.write(row, 0, date)
	sheet1.write(row, 1, visits)

	[visits, date] = getNumVisits(ad2)
	sheet2.write(row, 0, date)
	sheet2.write(row, 1, visits)

	[visits, date] = getNumVisits(ad3)
	sheet3.write(row, 0, date)
	sheet3.write(row, 1, visits)

	book.save("test.xls")
	row += 1
	time.sleep(30)


