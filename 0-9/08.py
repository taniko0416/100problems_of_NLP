# coding: utf-8

# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# ・英小文字ならば(219 - 文字コード)の文字に置換
# ・その他の文字はそのまま出力

# この関数を用い，英語のメッセージを暗号化・復号化せよ．

def cipher(target):
    result = ''
    for c in target:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result


target = input('文字列を入力してください-->')

# 暗号化
result = cipher(target)
print('暗号化:' + result)

# 復号化
result2 = cipher(result)
print('復号化:' + result2)

# 復号化で元に戻っているかチェック
if result2 != target:
    print('元に戻っていない！？')
else:
    print('OK')











# 入力の判定
# str.islower()を使います。
# 文字列中の英字（上記参照）全てが小文字で、かつそれが1文字以上ある場合はTrue、そうでない場合はFalseを返します。

# ord: アスキーコードを取得