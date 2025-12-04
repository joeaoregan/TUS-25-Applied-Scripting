# P24

import json
contacts = {"Ailbhe": "0861234567"}
json_string = json.dumps(contacts)
restored = json.loads(json_string)

print(json_string)
print()
print(restored)