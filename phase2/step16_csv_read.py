import csv

with open("phase2/receipt.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
