# coding: utf-8

# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．



def format_string(x, y, z):
    return '{hour}時の{target}は{value}'.format(hour=x, target=y, value=z)

x = 12
y = '気温'
z = 22.4
print(format_string(x,y,z))