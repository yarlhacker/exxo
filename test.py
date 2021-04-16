import csv,json


with open('fichers.csv','r') as f:
    reader = csv.DictReader(f)
    
    with open('fichers.json','w') as r:
        json.dump([ row for row in reader],r)
