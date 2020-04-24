import psycopg2
from psycopg2.extras import RealDictCursor

QUERY = '''
SELECT orders.order_id, orders.status, orders."createdAt", users.name, users.address, users.phone,
barcodemasters."ProductVariant", barcodemasters."BrandName",
barcodemasters."Price", orderitems.quantity
FROM orders
JOIN users
ON orders."userId" = users.id
JOIN orderitems
ON orders.id = orderitems."orderId"
JOIN barcodemasters
ON orderitems."barcodemasterId" = barcodemasters.id
AND orders."storeId" = 13
AND orders.status = 'RECEIVED'
AND orders.paid = true
ORDER BY orders.order_id, orders."createdAt" DESC;'''


connection = psycopg2.connect("dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
cursor = connection.cursor(cursor_factory=RealDictCursor)
cursor.execute(QUERY)
orders = cursor.fetchall()

print('order_id, order_status, user name, user address, user phone, product,brand, quantity, price, total, timestamp')
for order in orders:
    print(
        '"{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", {7}, {8}, {9}, "{10}"'.format
        (
            order['order_id'],
            order['status'],
            order['name'],
            order['address'],
            order['phone'],
            order['ProductVariant'],
            order['BrandName'],
            order['quantity'],
            order['Price'],
            (order['quantity'] * order['Price']),
            order['createdAt']
        )
    )

cursor.close()
connection.close()
