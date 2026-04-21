import json

with open("receipt.json","r",encoding="utf-8") as f:
    data = json.load(f)

print("読み込んだデータ:",data)
print("商品名:",data["商品"])
print("金額:",data["金額"],"円")
print("店:",data["店"])
print("日付:",data["日付"])