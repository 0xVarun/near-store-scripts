import psycopg2
from psycopg2.extras import RealDictCursor

products = [
    "9556420000041",
    "9556420000045",
    "9556420000055",
    "9556420000019",
    "9556420000049",
    "9556420000054",
    "9556420000044",
    "9556420000026",
    "9556420000048",
    "9556420000052",
    "9556420000051",
    "9556420000040",
    "9556420000066",
    "9556420000042",
    "9556420000015",
    "9556420000047",
    "9556420000043",
    "9556420000056",
    "9556420000046",
]

connection = psycopg2.connect("dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
cursor = connection.cursor(cursor_factory=RealDictCursor)

for p in products:
    print('[+] finding product : {}'.format(p))
    query = '''SELECT * FROM storescans WHERE box_id = 'e0512496BRND' AND barcode = '{0}';'''.format(p)
    cursor.execute(query)
    product = cursor.fetchone()
    if product is not None:
        print('[+] found product: {}'.format(p))
        cursor.execute('''UPDATE storescans SET visible = false WHERE box_id = 'e0512496BRND' AND barcode = '{0}';'''.format(p))
    else:
        print('[-] No such product in catalogue: {}'.format(p))
    

connection.commit()
cursor.close()
connection.close()