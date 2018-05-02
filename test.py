import requests
import time
url = "http://127.0.0.1:3000/data/"
with open("data.txt", "r") as f:
	for bin in f.readlines():
		print(bin)
		time.sleep(1)
		r = requests.get(url+str(bin))
