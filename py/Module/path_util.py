import os

'''
os.getcwd()  # 返回当前工作目录
os.listdir(path)   # 返回path指定的文件夹包含的文件或文件夹的名字的列表
os.mkdir(path)  # 创建文件夹
os.path.abspath(path)   # 返回绝对路径
os.path.basename(path)   # 返回文件名
os.path.isfile(path)   # 判断路径是否为文件
os.path.isdir(path)   # 判断路径是否为目录
'''

class PathUtil:
    def __init__(self, path):
        temp_path = path.strip('''"'"''')
        temp_path = os.path.abspath(temp_path)
        pair = os.path.split(temp_path)
        if "." in pair[1]:
            self.dir = pair[0]
            self.name = pair[1]
        else:
            self.dir = temp_path.rstrip("\\")
            self.name = None

    def is_file(self):
        return self.name != None

    def get_path(self):
        return self.dir if self.name == None else r"{}\{}".format(self.dir, self.name)

    def create_path(self, file_name):
        return r"{}\{}".format(self.dir, file_name)

if __name__ == "__main__":
    while True :
        path = PathUtil(input("输入路径："))
        print(path.get_path())
        print(path.create_path("test.txt"))
        if "Y" == input("输入Y结束：") :
            break