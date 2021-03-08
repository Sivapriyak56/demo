import csv
with open("new.csv","r")as f:
    r=csv.DictReader(f)
    for row in r:
        print(row)