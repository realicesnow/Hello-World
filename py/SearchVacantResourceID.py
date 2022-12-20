import os
import chardet

def get_encoding(path):
    with open(path, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def get_IDs(path):
    encode = get_encoding(path)
    ids = []
    with open( path, "r", encoding=encode ) as rsc:
        rows = rsc.readlines()
        for row in rows:
            row_list = row.split()
            if len(row_list) == 3 and row_list[0] == "#define":
                ids.append(int(row_list[2]))
        return ids

def GetFile():
    folder = input("ファイルパスを入力してください:")
    temp_path = folder.strip('''"'"''')
    return os.path.abspath(temp_path)

def SearchVacantIDs( file_path ):
    ids = list(set(get_IDs(file_path)))
    ids.sort()
    vacant_list = [] if ids[0] is 0 else [(0, ids[0]-1)]
    for index in range(len(ids)-2):
        if ids[index+1] - ids[index] > 1:
            vacant_list.append((ids[index]+1, ids[index+1]-1))

    return vacant_list

def PrintVacantIds( file_path ):
    vacant_list = SearchVacantIDs( file_path )
    print("空いているID番号:")
    for pair in vacant_list:
        if ( pair[0] == pair[1] ):
            print("{}".format(pair[0]))
            continue
        print("{}~{}".format(pair[0], pair[1]))

if __name__ == "__main__":
    print("***リソースファイルの空いているID番号を探します。***")
    while True :
        rsc = GetFile()
        PrintVacantIds( rsc )
        if "q" == input("qを入力して終了:") :
            break
