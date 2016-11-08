import requests
import xlwt

def findAttribute(attributes, value):
	for attribute in attributes:
		if attribute['id'] == value:
			return attribute['value_name']
			break
	return 'No especifica'

# r = requests.get('https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&')

# response = r.json()
# totalAds = response['paging']['total']

#Depa->Renta->DF
# endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ'
#Depa->Renta->DF->Cuahtemoc
# endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0NVQTczMTI'
#Depa->Renta->DF->Alvaro Obregon
endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0FMVjY3MDg'

ads = []
MAX_ADDS = 800
# #200 is the limit of results given by API
API_LIMIT = 200
for offset in range(0, MAX_ADDS, API_LIMIT):
	print 'Calculating number of adds:',round((float(offset+API_LIMIT)/MAX_ADDS)*100), '% complete'
	r = requests.get(endpoint+'&offset='+str(offset)+'&limit='+str(API_LIMIT))
	response = r.json()
	results = response['results']
	for result in results:
		ads.append(result['id'])

print 'Total ads:',len(ads)

#Create Excel book
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
#Add headers
sheet1.write(0, 0, "id")
sheet1.write(0, 1, "Precio")
sheet1.write(0, 2, "Moneda")
sheet1.write(0, 3, "Link")
sheet1.write(0, 4, "Delegacion")
sheet1.write(0, 5, "Colonia")
sheet1.write(0, 6, "Recamaras")
sheet1.write(0, 7, "Antiguedad")
sheet1.write(0, 8, "m2 de construccion")
sheet1.write(0, 9, "m2 de terreno")

print 'Requesting details of', len(ads), 'ads'

row = 1
for add in ads:
	#Brings info for that item
	print 'Requesting add', row, 'of', len(ads), round((float(row)/len(ads))*100),'% complete'

	r = requests.get('https://api.mercadolibre.com/items/'+add, timeout=2500)
	depa = r.json()

	#insert data
	sheet1.write(row, 0, depa['id'])
	sheet1.write(row, 1, depa['price'])
	sheet1.write(row, 2, depa['currency_id'])
	sheet1.write(row, 3, depa['permalink'])
	sheet1.write(row, 4, depa['location']['city']['name'])
	sheet1.write(row, 5, depa['location']['neighborhood']['name'])
	sheet1.write(row, 6, findAttribute(depa['attributes'], 'MLM1472-AMBQTY'))
	sheet1.write(row, 7, findAttribute(depa['attributes'], 'MLM1472-ANTIG'))
	sheet1.write(row, 8, findAttribute(depa['attributes'], 'MLM1472-MTRS'))
	sheet1.write(row, 9, findAttribute(depa['attributes'], 'MLM1472-MTRSTOTAL'))

	#Next row
	row += 1

book.save("MetrosCubicos.xls")


	