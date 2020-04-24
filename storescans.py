import sys
import json
import time
import math
import string
import random
import urllib.error
import urllib.parse
import urllib.request

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
    "9556420000169"
]

boxId = 'e0512496BRND'

session_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

payload = {
	"session_id": session_id,
	"box_id": boxId,
	"length": len(barcodes),
	"barcode": barcodes,
	"UTS": math.trunc(time.time()),
	"Agent": "PythonScript",
	"switch_state": 0,
	"status": [
		1,
		0,
		1395,
		1395
	]
}

url = "http://ekastaplatform.com:3000/v1/send"
req = urllib.request.Request(url, headers={'Content-Type': 'application/json'}, method="POST", data=json.dumps(payload).encode("utf-8"))
try:
	res = json.loads(urllib.request.urlopen(req).read().decode())
	print(res)
except urllib.error.HTTPError as e:
	print(e)
	print('HTTP Error')
