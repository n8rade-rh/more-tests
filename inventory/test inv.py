#!/usr/bin/python3

import json

with open('inventory/inventory.json', 'r') as f:
  data = json.load(f)

print(json.dumps(data))
