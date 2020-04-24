import psycopg2
from psycopg2.extras import RealDictCursor

barcodes = [
    "9556420000150",
    "9556420000151",
    "9556420000152",
    "9556420000153",
    "9556420000154",
    "9556420000155",
    "9556420000156",
    "9556420000157",
    "9556420000158",
    "9556420000159",
    "9556420000160",
    "9556420000161",
    "9556420000162",
    "9556420000163",
    "9556420000173",
    "9556420000164",
    "9556420000171",
    "9556420000174",
    "9556420000170",
    "9556420000172",
    "9556420000165",
    "9556420000166",
    "9556420000167",
    "9556420000168",
    "9556420000169",
]

connection = psycopg2.connect("dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432")
cursor = connection.cursor(cursor_factory=RealDictCursor)
query = '''SELECT * FROM barcodemasters WHERE "BarCode" = '{0}';'''

for barcode in barcodes:
    Q = query.format(barcode)
    cursor.execute(Q)
    product = cursor.fetchone()
    if product is None:
        print(barcode)
    else:
        print('A: {}'.format(barcode))

cursor.close()
connection.close()