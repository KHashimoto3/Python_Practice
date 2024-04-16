year = int(input("あなたの生まれた年を西暦で入力してください"))
if year <= 1988:
    print("昭和" + str(year - 1988) + "年ですね")
elif year <= 2018:
    print("平成" + str(year - 1988) + "年ですね")
else:
    print("令和" + str(year - 2018) + "年ですね")