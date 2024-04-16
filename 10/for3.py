# 途中でループを抜ける場合
for i in range(10):
    if i == 5:
        break
    print("アリ", end="")
else:
    print("アリーヴェデルチ！（さよならだ）")