# hightemp.txtは，日本の最高気温の記録を
# 「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
# 以下の処理を行うプログラムを作成し，
# hightemp.txtを入力ファイルとして実行せよ．
# さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．


with open('col1.txt') as col1_file, \
        open('col2.txt') as col2_file, \
        open('merge.txt', mode='w') as out_file:
        for col1_line, col2_line in zip(col1_file, col2_file):
            out_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')

# name_list = ["Jhon", "Mike", "Bob"]
# age_list = [23, 31, 28]
 
# for (name, age) in zip(name_list, age_list):
#     print str(name) + ":" + str(age)
