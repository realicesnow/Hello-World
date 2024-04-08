import os
import subprocess
import sys

def compile_toms(file_path):
    command = [r'C:\Program Files\Taiwa\Jissun\Tomc.exe', file_path]
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # 出力を表示
    print("Compile : {}".format( file_path) )
    print(result.stdout)
    # エラーがあれば表示
    if result.stderr:
        print(result.stderr)

def compile_dependent_toms(file_path, processed_files):
    if not os.path.exists(file_path):
        print("ファイル{}が存在しません。".format( file_path ))
        processed_files.add(file_path)
        return
    
    # ファイルを開いて import 文を検索する
    with open(file_path, 'r', ) as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('import'):
                # import 文からファイル名を取得する
                dependency = line.split('"')[1]
                dependency_path = os.path.join(os.path.dirname(file_path), dependency + '.toms')
                # 依存するファイルがまだ処理されていないかどうかを確認する
                if dependency_path not in processed_files:
                    # 依存するファイルを再帰的にコンパイルする
                    compile_dependent_toms(dependency_path, processed_files)
        # 自身をコンパイルする
        compile_toms(file_path)
        # コンパイルされたファイルを処理済みのファイルに追加する
        processed_files.add(file_path)

def GetTomsListToCompile():
    param_file_path = r"{}\{}".format( os.getcwd(), "TomsListToCompile.txt" )
    print('''
    {}からコンパイルするTomsファイルのフルパスのリストを読み込みます。読み込み失敗の場合は手動入力とします。
    '''.format(param_file_path))

    toms_files = []
    if not os.path.exists(param_file_path):
        return toms_files
    
    with open(param_file_path, 'r') as f:
        for line in f:
            temp_path = line.strip()
            temp_path = temp_path.strip('''"'"''')
            file_to_compile = os.path.abspath(temp_path)
            if file_to_compile.endswith('.toms'):
                toms_files.append(file_to_compile)
    return toms_files

def GetFile():
    input_str = input( "コンパイルするTomsファイルのフルパスを入力してください。qを入力する場合終了\n" )
    if input_str == "q":
        return input_str
    
    temp_path = input_str.strip('''"'"''')
    return os.path.abspath(temp_path)

if __name__ == "__main__":    
    # コンソール引数を取得し、メインのファイルとして処理する
    if len(sys.argv) > 1:
        compile_dependent_toms(sys.argv[1], set())
    else:
        print(".tomsファイルをコンパイルする")
        toms_files = GetTomsListToCompile()
        if toms_files :
            for toms_file in toms_files:
                compile_dependent_toms(toms_file, set())
        else:
            while True :
                input_str = input( "コンパイルするTomsファイルのフルパスを入力してください。qを入力する場合終了\n" )
                if "q" == input_str :
                    break
                temp_path = input_str.strip('''"'"''')
                input_str = os.path.abspath(temp_path)
                compile_dependent_toms(input_str, set())