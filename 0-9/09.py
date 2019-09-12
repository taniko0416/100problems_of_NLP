# coding: utf-8


# スペースで区切られた単語列に対して ，
# 各単語の先頭と末尾の文字は残し ，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ ．
# ただし ， 長さが４以下の単語は並び替えないこととする ．
# 適当な英語の文 （ 例えば
# "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# ）を与え，その実行結果を確認せよ．


import random

def Typoglyemia(target):
    result = []
    for word in target.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            chr_list = list(word[1:-1])
            random.shuffle(chr_list)
            result.append(word[0] + ''.join(chr_list) + word[-1])
    return ' '.join(result)

target = input('文字列を入力してください--> ')

result = Typoglyemia(target)
print('変換検索:' + result)

# random.shuffle(x[, random])
# シーケンス x をインプレースにシャッフルします。
# in-place 既存の物を環境に残したまま

# 多くの文字列を結合するのに最も効率的な方法は何ですか ？ ¶
# chunks = []
# for s in my_strings:
#     chunks.append(s)
# result = ''.join(chunks)


# str.join(iterable)
# iterable中の文字列を結合した文字列を返します 。
# test = ['ab', 'c', 'de']
# result = ''.join(test)
# print(result) // abcde
