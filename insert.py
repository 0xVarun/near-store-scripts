import json
import psycopg2

if __name__ == '__main__':
	data = None
	with open('22042020.json', 'r') as products:
		data = json.loads(products.read())

	conn = psycopg2.connect('dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432')
	cursor = conn.cursor()

	for index, product in enumerate(data):
		# print('{0}: inserting {1} with barcode {2}'.format(index + 1, product['ProductVariant'], product['BarCode']))
		cursor.execute('''select * from barcodemasters where "BarCode" = '{0}';'''.format(product['BarCode']))
		ext = cursor.fetchone()
		id = ext[0]
		print('{0}: inserting {1} with barcode {2} with id {3} into new_barcodemaster'.format(index + 1, product['ProductVariant'], product['BarCode'], id))
		# QUERY1 = '''INSERT INTO barcodemasters (id, "ProductVariant", "ProductGroup", "ProductCategory", "BarCode", "ProductType", url, "Company", "BrandName", "Price", "createdAt", "updatedAt", image_front, image_back, image_1, image_2, image_3, image_4) VALUES (nextval('barcodemasters_id_seq'), '{variant}', '{group}', '{category}', '{barcode}', '{ptype}', null, '{comp}', '{bname}', '{price}', current_timestamp, current_timestamp, '{imagef}', null, null, null, null, null);'''.format(
		# 		variant=product["ProductVariant"],
		# 		group=product["ProductGroup"],
		# 		category=product["ProductCategory"],
		# 		barcode=product["BarCode"],
		# 		ptype=product["ProductType"],
		# 		comp=product["Company"],
		# 		bname=product["BrandName"],
		# 		price=product["Price"],
		# 		imagef=product["image_front"]
		# 	)
		QUERY2 = '''INSERT INTO new_barcodemaster (id, "ProductVariant", "ProductGroup", "ProductCategory", "BarCode", "ProductType", url, "Company", "BrandName", "Price", "createdAt", "updatedAt", image_front, image_back, image_1, image_2, image_3, image_4) VALUES ({id}, '{variant}', '{group}', '{category}', '{barcode}', '{ptype}', null, '{comp}', '{bname}', '{price}', current_timestamp, current_timestamp, '{imagef}', null, null, null, null, null);'''.format(
				id=id,
				variant=product["ProductVariant"],
				group=product["ProductGroup"],
				category=product["ProductCategory"],
				barcode=product["BarCode"],
				ptype=product["ProductType"],
				comp=product["Company"],
				bname=product["BrandName"],
				price=product["Price"],
				imagef=product["image_front"]
			)
		# cursor.execute(QUERY1)
		cursor.execute(QUERY2)

	conn.commit()
	cursor.close()
	conn.close()