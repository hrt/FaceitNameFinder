import urllib3
import json
from string import ascii_lowercase
from collections import namedtuple

urllib3.disable_warnings()
http = urllib3.PoolManager()

for x in ascii_lowercase:
	for y in ascii_lowercase:
		for z in ascii_lowercase:
			username = x + y + z
			response = http.request('GET', 'https://api.faceit.com/core/v1/nicknames?nickname=' + username)
			obj = json.loads(response.data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
			if obj.message == "Nickname is available":
				print("[~] Found: " + username)
			

