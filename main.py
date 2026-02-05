import json
import csv
import pandas as pd

# THIS IS BASIC SYNTAX EVERYONE SHOULD KNOW FOR AUTOMATED SCRIPTS!!!

#READ JSON FILE
with open('file.json', 'r') as f:
    data = json.load(f)

# WRITE JSON FIKLE
with open('output.json', 'w') as f:
    json.dump(data, f, indent=2)

# access nested data
value = data['key']['nested_key']

# safe access with default
value = data.get('key', 'default')

# ITERATE THROUGH LIST OF DICTS
for item in data:
    print(item['field'])

#FILE OPERATIONS
with open('file.txt', 'r') as f:
    context = f.read()

#READ CSV
with open('file.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['column_name'])

#read with pandas
df = pd.read_csv('file.csv')


###############################################


