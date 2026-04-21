#22 Step22 レシートデータをJSONに保存する

import json

receipts = [
    {"日付":"2026-04-21","商品名":"卵","金額":198,"店名":"イオン"},
    {"日付":"2026-04-21","商品名":"大根","金額":98,"店名":"イオン"},
    {"日付":"2026-04-21","商品名":"牛乳","金額":178,"店名":"イオン"}
   ]

with open("receipts.json","w",encoding="utf-8") as f:
    json.dump(receipts,f,ensure_ascii=False,indent=2)
print("receipts.json に保存しました")
