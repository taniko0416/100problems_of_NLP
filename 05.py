# 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．

def n_gram(target, n):
  # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
  result = []
  
# 単語（文字）に分けている
  for i in range(0,len(target) - n + 1):
        result.append(target[i: i + n])
  
  return result

# ※空白も一文字と認識される
target = "I am an NLPer"

words_target = target.split(' ')

# 単語bu-gram
result = n_gram(words_target, 2)

# 文字bi-gram
result2 = n_gram(words_target,2)

result3 = n_gram(words_target,3)
print(result)
print(result2)
print(result3)




# :の使い方
# a = list(range(0,10)) 
# a[2] #2
# a[2:8] #[2, 3, 4, 5, 6, 7]
# # i を省略すると始点から
# a[:6] #[0, 1, 2, 3, 4, 5]
# # j を省略すると要素の一番最後まで
# a[7:] #[7, 8, 9]
# a[-1] #9
# # -8番目から-6(-5-1)番目の要素を取り出す
# a[-8:-5] #[2, 3, 4] （使わない）
# # 始点から-6(-5-1)番目の要素を取り出す
# a[:-6] #[0, 1, 2, 3] （ほぼ使わない）
# # -8番目から終点までの要素を取り出す
# a[-2:] #[8, 9] （拡張子の取り出しなどよく使う）
