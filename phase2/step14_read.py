#Step 14 : ファイルを読み込む

f=open("test.txt","r",encoding="utf-8")
lines=f.readlines()
f.close()

for line in lines:
    print(line.strip())

