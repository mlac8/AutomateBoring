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

#syntax i should memorize COLD

with open("file.json", "w") as f:
    data = json.load(f)

for item in data:
    print(item["keyh"])

item.get("key")
item.get("nested, {}").ge("key")

result = []
result[key] = value

sum(item["numbers"])
len(item["numbers"])

###########

# DRILL TIME
### return a list of usernames where sum > 40:
with open('file.json', 'w') as f:
    data = json.load(f)
    for item in data:
        sum(item["numbers"])
 ### WRONG what we want to see is



with open('file.json', 'r') as f:
    data = json.load(f)

result = [] #create empty list

for item in data:
    total = sum(item["scores"])
    if total > 40:
        result.append(item["user"]["name"])

print(result)

### return a DICTIONARY mapping username to their avg score
with open('file.json', 'r') as f:
    data = json.load(f)

mean = []

# iterates through data and scrapes for mean

for item in data:
    mean = mean.append(item["scores"])

print(mean)
# THIS IS ALSO INCORRECT. THE CORRECT ANSWER IS:

with open('file.json', 'r') as f:
    data = json.load(f)

result = {} # THIS IS A DICT. YOU DON'T WANT A [] list for this question

for item in data:
    name = item["user"]["name"]
    scores = item["scores"]
    avg = sum(scores) / len(scores)
    result[name] = avg

print(result)
# remember: 1) EXTRACT NAME, 2) EXTRACT LIST, 3) COMPUTE, 4) PUT INTO RESULT

### Return a list of names of users OLDER THAN 30 whose highest score is > 25
with open('file.json', 'r') as f:
    data = json.load(f)

result = []
