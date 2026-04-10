import csv

#書き込むデータ(リストのリスト)
rows = [
    ["商品","金額","店"],
    ["大根","98","イオン"],
    ["卵","198","イオン"],
    ["牛乳","148","イオン"],
    ]

with open("phase2/receipt.csv","w",newline="",encoding="utf-8")as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("receipt.csv に書き込みました")