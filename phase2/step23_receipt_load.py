import json

with open("receipts.json","r",encoding="utf-8") as f:
    receipts = json.load(f)

for receipt in receipts:
    print(receipt["日付"],receipt["店名"],receipt["商品名"],receipt["金額"],"円")
