import json

# THIS IS BASIC SYNTAX EVERYONE SHOULD KNOW FOR AUTOMATED SCRIPTS!!!

#READ JSON FILE
with open('file.json', 'r') as f:
    data = json.load(f)

# WRITE JSON FIKLE
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

