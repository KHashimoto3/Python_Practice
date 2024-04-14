# 論理演算子（ブール演算子）
# 論理積
age = int(input("きみの年齢は？"))
if age >= 12 and age <= 15:
    print("きみは中学生だな")
else:
    print("きみは中学生ではないな")

# 論理和
if age <= 12 or age >= 15:
    print("きみは中学生ではないな")
else:
    print("きみは中学生だな")

# 否定（not）
if not age >= 20:
    print("きみは未成年だな")
else:
    print("君は成人だな")
