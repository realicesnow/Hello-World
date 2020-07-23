import glob
import os
import csv
import chardet

def GetFilesList(folder, ext):
    search_key = r"{}\{}".format(folder, "*" + ext)
    return sorted(glob.glob(search_key))

def GetFolder():
    folder = input("フォルダパスを入力してください:")
    temp_path = folder.strip('''"'"''')
    temp_path = os.path.abspath(temp_path)
    pair = os.path.split(temp_path)
    return pair[0] if "." in pair[1] else temp_path.rstrip("\\")

def ToInt(string):
    try:
        value = int(string)
        return value
    except Exception:
        return None

# 指定したフォルダ内のある拡張子のファイルの数値部を同じ桁数のように0を埋める
def RenameFilesName( prefix = "icon-", ext = ".png", digits = 3 ):
    folder = GetFolder()
    file_list = GetFilesList( folder, ext )
    no_renamed_list = []
    for file_path in file_list :
        pair = os.path.split(file_path)
        rsplit_name = pair[1].rstrip(ext)
        number = ToInt(rsplit_name.lstrip(prefix))
        if number is None:
            no_renamed_list.append( file_path )
            continue
        new_file_path = "{0}\{1}{2:0={3}}{4}".format(pair[0], prefix, number, digits, ext)
        os.rename( file_path, new_file_path )

    if len(no_renamed_list) > 0 :
        print("リネーム失敗のファイル: {}".format(len(no_renamed_list)))
        for failure_path in no_renamed_list:
            print("  {}".format(failure_path))
    else :
        print("リネーム完了。")

def get_encoding(path):
    with open(path, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def get_csv_rows(path):
    encode = get_encoding(path)
    with open(path, newline='', encoding=encode) as f:
        reader = csv.reader(f)
        rows = list(reader)
        return rows

def GetRenameFilesNameParamsFromCSV(param_file_path):
    params = { "prefix" : None, "ext": None, "digits": None }
    if not os.path.exists(param_file_path):
        print("CSVファイルは存在しません。")
        return params
    rows = get_csv_rows(param_file_path)
    print("パラメータを読み込みました。: \n    {}".format(rows))
    for row in rows:
        if "prefix" == row[0]:
            params["prefix"] = row[1]
        if "ext" == row[0]:
            params["ext"] = row[1]
        if "digits" == row[0]:
            params["digits"] = row[1]
    return params

def GetRenameFilesNameParams():
    param_file_path = r"{}\{}".format( os.getcwd(), "RenameFilesNameParams.csv" )
    print('''
    {}からパラメータを読み込みます。読み込み失敗の場合は手動入力します。
        prefix: ファイル名の数値部の前の文字。例: "icon-"
        ext   : ファイルの拡張子。例: ".png"
        digits: リネーム後ファイル名の数値部の桁数。例: 3
    '''.format(param_file_path))
    params_dict = GetRenameFilesNameParamsFromCSV(param_file_path)
    for key in params_dict.keys():
        if params_dict[key] == None :
            params_dict[key] = input("{} を入力してください。:".format(key))
    return params_dict

if __name__ == "__main__":
    print("指定したフォルダ内のある拡張子のファイルの数値部を同じ桁数のように0を埋める。")
    params_dict = GetRenameFilesNameParams()
    while True :
        RenameFilesName( prefix=params_dict["prefix"], ext=params_dict["ext"], digits=params_dict["digits"] )
        if "q" == input("qを入力して終了:") :
            break