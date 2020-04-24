import json
import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect("dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
cursor = connection.cursor(cursor_factory=RealDictCursor)

data = []
wiz = open('wizoot.json', 'r')
try:
    data = json.loads(wiz.read())
except:
    pass

'''
6. Dairy Products -> Dairy_Products
8. Home Needs -> HomeNeeds
9. Fresh & Frozen Food -> Fresh_FrozenFood
10. Baby & Kids -> Baby_kids
11. Pet Care -> PetCare
'''

query = '''SELECT * FROM barcodemasters WHERE id = 247679 OR id = 247684;'''

'''
126124 OR id = 126168 OR id = 130407 OR id = 133424
'''

cursor.execute(query)
products = cursor.fetchall()

for p in products:
    # payload = {
    #     'name': p['name'],
    #     'group': p['group'],
    #     'category': p['category'],
    #     'barcode': p['barcode'],
    #     'type': p['type'],
    #     'company': p['company'],
    #     'brand': p['brand'],
    #     'url': p['url'],
    #     'box_id': 'DEMO_VIR_BOX',
    #     'count': p['count'],
    #     'price': p['price'],
    #     'endpoint': 'send',
    # }
    payload = {
        'name': p['ProductVariant'],
        'group': 'Home Care & Kitchen',
        'category': 'Home Care & Kitchen',
        'barcode': p['BarCode'],
        'type': 'Home Care & Kitchen',
        'company': p['Company'],
        'brand': p['BrandName'],
        'url': p['image_front'],
        'box_id': 'DEMO_VIR_BOX',
        'count': 0,
        'price': p['Price'],
        'endpoint': 'send',
    }
    data.append(payload)

fjs = json.dumps(data, indent=4)
print(fjs)
# wiz.write(fjs)
wiz.close()
connection.commit()
cursor.close()
connection.close()