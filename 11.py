# hightemp.txtは，日本の最高気温の記録を
# 「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
# 以下の処理を行うプログラムを作成し，
# hightemp.txtを入力ファイルとして実行せよ．
# さらに，同様の処理をUNIXコマンドでも実行し，
# プログラムの実行結果を確認せよ．


file_name = "hightemp.txt"
with open(file_name) as data_file:
    for line in data_file:
        print(line.replace('\t', ' '), end='')
            


# \tはたぶのこと
# [print]の[end]について