# 論理演算市を組み合わせて使う
age = int(input("きみの年齢は？"))
ans = input("きみは就学・就労・職業訓練のいずれかを行なっているか？")

if age >= 15 and age <= 34 and not ans == "yes":
    print("NEET!!!")
else:
    print("お帰りください。")