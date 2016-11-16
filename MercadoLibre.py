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
# endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0FMVjY3MDg'

#Santa Fe (Alvaro Obregon)
#endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0FMVjY3MDg&neighborhood=TUxNQlNBTjQzOTBB'

#Polanco (Miguel Hidalgo) Polanco IV Seccion
#endpoint1 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTDIwNUQ'
#Polanco Chapultepec
#endpoint2 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTDMwOTk'
#Polanco I Seccinn
#endpoint3 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTDlDNzQ'
#Polanco III Seccinn
#endpoint4 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTEU3RTk'
#Polanco II Seccinn
#endpoint5 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTDhFRDU'
#Polanco V Seccinn
#endpoint6 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTEQ0OTE'
#Polanco Reforma
#endpoint7 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBPTDM4OTE'
#Palmas Polanco
#endpoint8 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg&neighborhood=TUxNQlBBTDcxMzc'

#Toda la delegacion Benito Juarez
#endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0JFTjM2MjQ'
#Toda la miguel hidalgo
endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ01JRzU0Mjg'
#Toda la alvaro obregon
endpoint2 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0FMVjY3MDg'
#Toda cuajimalpa de morelos
endpoint3 = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0NVQTgxNTY'

#Juarez (Cuautemoc)
#endpoint = 'https://api.mercadolibre.com/sites/MLM/search?category=MLM1479&state=TUxNUERJUzYwOTQ&city=TUxNQ0NVQTczMTI&neighborhood=TUxNQkpVwTM5MDY'

ads = []
MAX_ADDS = 2322 + 200
# #200 is the limit of results given by API
API_LIMIT = 200
for offset in range(0, MAX_ADDS, API_LIMIT):
	print 'Calculating number of adds:',round((float(offset+API_LIMIT)/MAX_ADDS)*100), '% complete'
	r = requests.get(endpoint3+'&offset='+str(offset)+'&limit='+str(API_LIMIT))
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
sheet1.write(0, 6, "BEDROOMS")
sheet1.write(0, 7, "PROPERTY_AGE")
sheet1.write(0, 8, "COVERED_AREA")
sheet1.write(0, 9, "TOTAL_AREA")
sheet1.write(0, 10, "FULL_BATHROOMS")
sheet1.write(0, 11, "FURNISHED")
sheet1.write(0, 12, "HAS_KITCHEN")
sheet1.write(0, 13, "HAS_BALCONY")
sheet1.write(0, 14, "PARKING_LOTS")
sheet1.write(0, 15, "HAS_DINNING_ROOM")
sheet1.write(0, 16, "HAS_HALF_BATH")
sheet1.write(0, 17, "HAS_TERRACE")
sheet1.write(0, 18, "HAS_GYM")
sheet1.write(0, 19, "HAS_MULTIPURPOSE_ROOM")
sheet1.write(0, 20, "HAS_PARTY_ROOM")
sheet1.write(0, 21, "HAS_SECURITY")
sheet1.write(0, 22, "MAINTENANCE_FEE")
sheet1.write(0, 23, "FLOORS")


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
	sheet1.write(row, 6, findAttribute(depa['attributes'], 'BEDROOMS'))
	sheet1.write(row, 7, findAttribute(depa['attributes'], 'PROPERTY_AGE'))
	sheet1.write(row, 8, findAttribute(depa['attributes'], 'COVERED_AREA'))
	sheet1.write(row, 9, findAttribute(depa['attributes'], 'TOTAL_AREA'))
	sheet1.write(row, 10, findAttribute(depa['attributes'], 'FULL_BATHROOMS'))
	sheet1.write(row, 11, findAttribute(depa['attributes'], 'FURNISHED'))
	sheet1.write(row, 12, findAttribute(depa['attributes'], 'HAS_KITCHEN'))
	sheet1.write(row, 13, findAttribute(depa['attributes'], 'HAS_BALCONY'))
	sheet1.write(row, 14, findAttribute(depa['attributes'], 'PARKING_LOTS'))
	sheet1.write(row, 15, findAttribute(depa['attributes'], 'HAS_DINNING_ROOM'))
	sheet1.write(row, 16, findAttribute(depa['attributes'], 'HAS_HALF_BATH'))
	sheet1.write(row, 17, findAttribute(depa['attributes'], 'HAS_TERRACE'))
	sheet1.write(row, 18, findAttribute(depa['attributes'], 'HAS_GYM'))
	sheet1.write(row, 19, findAttribute(depa['attributes'], 'HAS_MULTIPURPOSE_ROOM'))
	sheet1.write(row, 20, findAttribute(depa['attributes'], 'HAS_PARTY_ROOM'))
	sheet1.write(row, 21, findAttribute(depa['attributes'], 'HAS_SECURITY'))
	sheet1.write(row, 22, findAttribute(depa['attributes'], 'MAINTENANCE_FEE'))
	sheet1.write(row, 23, findAttribute(depa['attributes'], 'FLOORS'))

	#Next row
	row += 1

book.save("16NOV16-Cuajimalpa.xls")


	