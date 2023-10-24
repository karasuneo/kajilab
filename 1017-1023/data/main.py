import os
import re

# 同じディレクトリの中にあるディレクトリ名を取得
dirs = os.listdir("./")
dirs.remove("main.ipynb")
dirs.remove("main.py")
dirs.remove(".DS_Store")

for path in dirs:
    # 以下のディレクトリの中のファイル名を取得
    files = os.listdir(path)

    # ファイル名を表示
    for file in files:
        # ファイル名から数字と_と-を削除して保存
        file_name = file.replace(" ", "").replace("-", "").replace("_", "")
        file_name = re.sub("[0-9]", "", file_name)
        # ファイル名を上書き保存
        os.rename(path + "/" + file, path + "/" + file_name)
