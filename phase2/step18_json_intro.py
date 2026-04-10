# Step 18: JSONって何？

import json

#Pythonの辞書　(Step6で使ったもの)
receipt = {
    "商品":"大根",
    "金額":"98",
    "店":"イオン",
    "日付":"2026-04-11"
  }

#辞書をJSON文字列に変換してみる
json_text = json.dumps(receipt,ensure_ascii=False,indent=2)
print("JSON形式：")
print(json_text)
print()

#JSON文字列を辞書に戻してみる
receipt2 = json.loads(json_text)
print("辞書に戻した結果:")
print(receipt2["商品"])
print(receipt2["金額"])


