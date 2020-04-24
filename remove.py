import psycopg2

barcodes = [
	"9556420000040",
	"9556420000041",
	"9556420000042",
	"9556420000043",
	"9556420000044",
	"9556420000045",
	"9556420000046",
	"9556420000047",
	"9556420000048",
	"9556420000049",
	"9556420000050",
	"9556420000051",
	"9556420000052",
	"9556420000053",
	"9556420000054",
	"9556420000055",
	"9556420000056",
	"9556420000066",
]

conn = psycopg2.connect('dbname=Ekasta host=db.ekastaplatform.com user=ekasta password=beacon5791 port=5432')
cursor = conn.cursor()

for index, barcode in enumerate(barcodes):
	print('[{0}] deleting {1}'.format(index + 1, barcode))
	cursor.execute("delete from storescans where barcode = '{0}' and box_id = 'e0512496BRND';".format(barcode))

conn.commit()
cursor.close()
conn.close()