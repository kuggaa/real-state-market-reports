import requests
import xlwt

#Depa->Renta->DF->Cuautemoc
endpoint = 'https://webapi.segundamano.mx/nga/api//v1.1/public/klfst?lang=es&category=1040&region=11&municipality=295&estate_type=1&lim=3000'
#Depa->Renta->DF->Alvaro Obregon
endpoint2 = 'https://webapi.segundamano.mx/nga/api//v1.1/public/klfst?lang=es&category=1040&region=11&municipality=290&estate_type=1&lim=3000'

r = requests.get(endpoint)
response = r.json()
ads = response['list_ads']

r = requests.get(endpoint2)
response = r.json()
ads2 = response['list_ads']

print 'Total of ads:', len(ads) + len(ads2)
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
sheet1.write(0, 7, "m2")

row = 1
for element in ads:
	ad = element['ad']

	print 'Saving number', row, 'out of', len(ads), 'id:', ad['ad_id']
	sheet1.write(row, 0, ad['ad_id'])
	if 'list_price' not in ad:
		sheet1.write(row, 1, 'No especifica')
		sheet1.write(row, 2, 'No especifica')
	else:
		sheet1.write(row, 1, ad['list_price']['price_value'])
		sheet1.write(row, 2, ad['list_price']['currency'])
	sheet1.write(row, 3, ad['share_link'])
	sheet1.write(row, 4, ad['locations'][0]['locations'][0]['label'])
	if 'locations' not in ad['locations'][0]['locations'][0]:
		sheet1.write(row, 5, 'No especifica')
	else:
		sheet1.write(row, 5, ad['locations'][0]['locations'][0]['locations'][0]['label'])
	if 'rooms' not in ad['ad_details']:
		sheet1.write(row, 6, 'No especifica')
	else:
		sheet1.write(row, 6, ad['ad_details']['rooms']['single']['code'])
	if 'size' not in ad['ad_details']:
		sheet1.write(row, 7, 'No especifica')
	else:
		sheet1.write(row, 7, ad['ad_details']['size']['single']['code'])

	#Next row
	row += 1

for element in ads2:
	ad = element['ad']

	print 'Saving number', row, 'out of', len(ads)+len(ads2), 'id:', ad['ad_id']
	sheet1.write(row, 0, ad['ad_id'])
	if 'list_price' not in ad:
		sheet1.write(row, 1, 'No especifica')
		sheet1.write(row, 2, 'No especifica')
	else:
		sheet1.write(row, 1, ad['list_price']['price_value'])
		sheet1.write(row, 2, ad['list_price']['currency'])
	sheet1.write(row, 3, ad['share_link'])
	sheet1.write(row, 4, ad['locations'][0]['locations'][0]['label'])
	if 'locations' not in ad['locations'][0]['locations'][0]:
		sheet1.write(row, 5, 'No especifica')
	else:
		sheet1.write(row, 5, ad['locations'][0]['locations'][0]['locations'][0]['label'])
	if 'rooms' not in ad['ad_details']:
		sheet1.write(row, 6, 'No especifica')
	else:
		sheet1.write(row, 6, ad['ad_details']['rooms']['single']['code'])
	if 'size' not in ad['ad_details']:
		sheet1.write(row, 7, 'No especifica')
	else:
		sheet1.write(row, 7, ad['ad_details']['size']['single']['code'])

	#Next row
	row += 1

book.save("SegundaMano.xls")
