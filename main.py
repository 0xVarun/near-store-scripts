import json


with open('products.json', 'r') as p:
    data = json.loads(p.read())
    for d in data:
        print(d['BarCode'])