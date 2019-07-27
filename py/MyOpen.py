def ck_patch( path ):
    return path.strip('''"'"''')

#Test
path = ck_patch(input("请输入文件路径："))
file1 = open(path, 'r', encoding='utf-8')
filecontent = file1.read()
print(filecontent)
file1.close()
