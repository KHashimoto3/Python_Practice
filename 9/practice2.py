password = "1234"

line1 = input("パスワードを入力してください")
line2 = input("確認のためもう一度パスワードを入力してください")

if line1 == password and line2 == password:
    print("パスワードの認証に成功しました")
else:
    print("パスワードが違います")