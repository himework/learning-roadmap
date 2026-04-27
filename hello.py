print("レシート家計簿アプリを作るぞ！")

#step 3 :変数を使う
item = "大根"
price = 98
shop = "イオン"

print(item)
print(price)
print(shop)

#Step 4 :if文
if price >= 100 :
    print("高い買い物です")
else:
    print("安い買い物です")

#Step5 :for文
shopping_list = ["大根", "卵", "牛乳"]

for item in shopping_list:
    print(item)

#Step6 : 辞書(dict)
receipt = {"商品":"大根","金額": 98,"店":"イオン"}

print(receipt["商品"])
print(receipt["金額"])
print(receipt["店"])

print()

#Step 7 :関数(def)
def show_item(receipt):
    print(receipt["商品"])
    print(receipt["金額"])
show_item(receipt)




