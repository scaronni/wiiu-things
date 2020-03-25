#!/usr/bin/env python3

# usage: wiiu_titlekeys.py

import json
from urllib.request import Request, urlopen

keys_url = 'http://vault.titlekeys.ovh/json'
keys_filename = 'titlekeys.json'

print("Downloading {} to UTF-8 formatted {}...".format(keys_url, keys_filename))

request = Request(keys_url)
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)')
response = urlopen(request).read()
keys_json_raw = json.loads(response)
keys_json_formatted = json.dumps(keys_json_raw, indent=4)
keys_json_formatted = keys_json_formatted.encode('utf-8').decode('unicode-escape')

with open(keys_filename, "w") as f:
    f.write(keys_json_formatted)
