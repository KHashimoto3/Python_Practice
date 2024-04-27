print("問題：この本のタイトルはなんでしょう？")
print("1.Pythonの教科書")
print("2.ゼロから学ぶPython")
print("Pythonで学ぶプログラミング入門")

while True:
    ans = int(input("答えは？"))
    if ans == 3:
        print("正解！")
        break
    print("残念！")
