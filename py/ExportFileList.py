import glob
import os
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

# 指定したフォルダ内のある拡張子のファイルを[フォルダ名_FileList.txt]に出力
def ExportFileList():
    folder = GetFolder()
    ext = input('''
    ファイルの拡張子を入力してください。
        例：.jpeg
    ''')
    folder_name = folder.rsplit( "\\", 1 )[1]
    # export_file_path = r"{}\{}".format( os.getcwd(), "RenameFilesNameParams.csv" )
    export_file_path = os.getcwd() + "\\" + folder_name + "_FileList.txt"
    file_list = GetFilesList( folder, ext )
    if len(file_list) < 1:
        print("指定したフォルダ内{}ファイルは存在しません".format(ext))
        return

    with open(export_file_path, "w", encoding="utf-8") as f:
        for file_path in file_list :
            f.write(file_path)
            f.write("\n")

    print("{}に出力しました。".format(export_file_path))

if __name__ == "__main__":
    print("指定したフォルダ内のある拡張子のファイルリストを[フォルダ名_FileList.txt]に出力。")
    while True :
        ExportFileList()
        if "q" == input("qを入力して終了:") :
            break