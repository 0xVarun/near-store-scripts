import requests
import psycopg2
from urllib.parse import urlencode, quote_plus

conn = None
cur = None

try:
	conn = psycopg2.connect('dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432')
	cur = conn.cursor()

	users_ = cur.execute('''SELECT * FROM orders JOIN users ON orders."userId" = users.id WHERE orders."storeId" = 14 and orders.paid = true and orders.status = 'RECEIVED';''')
	users = cur.fetchall()

	sms = 'Thanks for using Near.Store. Your order {orderId} has been received. We appreciate your business. At this moment we are only accepting orders from Beau Monde CHS, other orders will be cancelled and money will be refunded. Thanks'

	for user in users:
		orderId = user[1]
		number = user[14]
		textMsg = sms.format(orderId=orderId)
		payload = urlencode({ 'Message': textMsg }, quote_via=quote_plus)
		if number:
			r = requests.get("""https://hapi.smsapi.org/SendSMS.aspx?UserName=Ekasta_live&password=Viva@5791&MobileNo={0}&SenderID=NEARST&CDMAHeader=NEARST&{1}""".format(number, payload))
			print(r.status_code)
			print(r.text)


except Exception as e:
	print(e)
finally:
	cur.close()
	conn.close()