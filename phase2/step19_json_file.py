#step19: jsonをファイルに保存・読み込み

import json

#保存するレシートデータ
receipt = {
    "商品":"大根",
    "金額":"98",
    "店":"イオン",
    "日付":"2026-04-14"
}
 #① jsonファイルに書き込む
with open("receipt.json","w",encoding="utf-8") as f:
    json.dump(receipt,f,ensure_ascii=False,indent=2)

print("receipt.json に保存しました")

    
    