# coding: utf-8

# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
# それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
# さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

def n_gram(target, n):
      # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  result = []
  
# 単語（文字）に分けている
  for i in range(0,len(target) - n + 1):
        result.append(target[i: i + n])
  
  return result


# setは行列を作る
set_x = set(n_gram('paraparaparadise',2))
print('X' + str(set_x))
set_y = set(n_gram('paragraph', 2))
print('Y' + str(set_y))

# 和集合
set_or = set_x | set_y
print('和集合:' + str(set_or))

# 積集合
set_and = set_x & set_y
print('積集合:' + str(set_and))

# 差集合
set_sub = set_x - set_y
print('差集合:' + str(set_sub))

print('seがXに含まれる:' + str('se' in set_x))
print('seがYに含まれる:' + str('se' in set_y))


# Python には、 集合 (set) を扱うためのデータ型もあります。
# 集合とは、重複する要素をもたない、順序づけられていない要素の集まりです。
#  Set オブジェクトは、和 (union)、積 (intersection)、
# 差 (difference)、対称差 (symmetric difference)といった数学的な演算もサポートしています。

# 中括弧、または set() 関数は set を生成するために使用することができます。注: 空集合を作成するためには set() を使用しなければなりません ({} ではなく)。後者は空の辞書を作成します。辞書は次のセクションで議論するデータ構造です。

# 簡単なデモンストレーションを示します:

# >>>
# >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# >>> print(basket)                      # show that duplicates have been removed
# {'orange', 'banana', 'pear', 'apple'}
# >>> 'orange' in basket                 # fast membership testing
# True
# >>> 'crabgrass' in basket
# False

# >>> # Demonstrate set operations on unique letters from two words
# ...
# >>> a = set('abracadabra')
# >>> b = set('alacazam')
# >>> a                                  # unique letters in a
# {'a', 'r', 'b', 'c', 'd'}
# >>> a - b                              # letters in a but not in b
# {'r', 'd', 'b'}
# >>> a | b                              # letters in a or b or both
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
# >>> a & b                              # letters in both a and b
# {'a', 'c'}
# >>> a ^ b                              # letters in a or b but not both
# {'r', 'd', 'b', 'm', 'z', 'l'}






# 指定の値を持つ要素がリストの中に含まれているかどうかを確認するには in 演算子を使用します。

# 値 in リスト

# リストの要素の中で指定した値と同じ値を持つ要素があった場合には式は True となります。
# なかった場合には False となります。

# 具体的には次のように記述します。
# >>> mylist = ["A", "B", "C", "D", "E"]
# >>> print("B" in mylist)
# True
# >>> print("G" in mylist)
# False
# >>>