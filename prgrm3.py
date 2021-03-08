import csv
with open("na.csv","r")as f:
    reader=csv.reader(f)
    for row in reader:
        print((row)