import os
import sys
import json
import pydoc
import datetime
import psycopg2
from tabulate import tabulate

REPORT = """\n\n\n\n\n\n==================================ORDER==================================
order-id: {orderId}
billAmount: {billAmount}
status: {status}
timestamp: {ts}

customer:
	name: {cname}
	phone: {cphone}
	address: {address}

{table}


===================================BILL===================================

billAmount: {billAmount}

===================================END===================================
\n\n\n\n\n\n
"""

def setConfirm(orders):
	connection = None
	cursor = None
	try:
		connection = psycopg2.connect("dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
		cursor = connection.cursor()
	except Exception as e:
		print(e)
	finally:
		if connection is not None:
			cursor.close()
			connection.close()

def process(orders):
	report = []
	for order in orders:
		print('[+] generating report for {} orderid'.format(order['order_id']))
		orderId = order['order_id']
		orderAmount = order['order_amount']
		orderStatus = order['order_status']
		timestamp = order['ts']
		name = order['user']['name']
		phone = order['user']['phone']
		address = order['user']['address']
		table = tabulate(
			order['products'],
			# headers=['Sr No.', 'Product Name', 'Quantity', 'Price', 'Total']
			headers=['Sr No.', 'Product Name', 'Quantity']
		)
		x1 = REPORT.format(
			orderId=orderId,
			billAmount=orderAmount,
			status=orderStatus,
			ts=timestamp,
			cname=name,
			cphone=phone,
			address=address,
			table=table
		)
		report.append(x1)

	REP = '\n'.join(x for x in report)
	filename = '{0}-orders.txt'.format(datetime.date.today().strftime('%d%m%Y'))
	with open(os.path.join('reports', filename), 'w') as rep_file:
		rep_file.write(REP)
	print('[+] report written to file {}'.format(filename))
	

def main():
	connection = None
	cursor = None
	ORDERS = []
	try:
		connection = psycopg2.connect("dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
		cursor = connection.cursor()
		cursor.execute('''SELECT * FROM orders WHERE "storeId" = 13 AND status != 'CONFIRMED' AND paid = true ORDER BY "createdAt" DESC;''')
		orders = cursor.fetchall()
		print('[+] found {} order(s)'.format(len(orders)))
		for order in orders:
			temp_order = {}
			orderDBId = order[0]
			userId = order[9]
			cursor.execute('''SELECT * FROM orderitems JOIN barcodemasters ON orderitems."barcodemasterId" = barcodemasters.id WHERE "orderId" = {0};'''.format(orderDBId))
			products = cursor.fetchall()
			temp_order['order_id'] = order[1]
			temp_order['order_amount'] = order[2]
			temp_order['order_status'] = order[3]
			temp_order['products'] = []
			temp_order['ts'] = order[6]
			print('[+] processing {} orderid'.format(order[1]))
			for index, product in enumerate(products):
				print('[+]\tadd {0} to order with id {1}'.format(product[9], order[1]))
				product_O = []
				product_O.append(index + 1)
				product_O.append(product[9])
				product_O.append(product[7])
				# product_O.append(product[17])
				# product_O.append(product[7] * product[17])
				temp_order['products'].append(product_O)
			cursor.execute('''SELECT * FROM users WHERE id = {0};'''.format(userId))
			user = cursor.fetchone()
			temp_order['user'] = {}
			temp_order['user']['name'] = user[2]
			temp_order['user']['phone'] = user[4]
			temp_order['user']['address'] = user[6]
			ORDERS.append(temp_order)
	except Exception as e:
		print(e)
	finally:
		if connection is not None:
			cursor.close()
			connection.close()
	
	process(ORDERS)

if __name__ == '__main__':
    main()
