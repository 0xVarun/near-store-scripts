import json
import psycopg2
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect("dbname=wizroots host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
cursor = connection.cursor(cursor_factory=RealDictCursor)

data = []
wiz = open('wizoot.json', 'r')
products = json.loads(wiz.read())

QUERY = '''
INSERT INTO storescans VALUES (nextval('storescans_id_seq'), '{name}', '{name}', '{group}', '{category}', '{barcode}', '{ptype}', '{company}', '{brand}', '{url}', '{box_id}', {count}, {price}, {price}, 'send', current_timestamp, current_timestamp)
'''

for p in products:
    f = QUERY.format(
        name=p['name'],
        group=p['group'],
        category=p['category'],
        barcode=p['barcode'],
        ptype=p['type'],
        company=p['company'],
        brand=p['brand'],
        url=p['url'],
        box_id=p['box_id'],
        count=p['count'],
        price=p['price']
    )
    print(f)

connection.commit()
cursor.close()
connection.close()