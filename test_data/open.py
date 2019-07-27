path = input("输入文件路径：")

file1 = open(r"{}".format(path),
             'r', encoding='utf-8')
filecontent = file1.read()
print(filecontent)
file1.close()

add_str = input("追加内容：")
file1 = open(r"{}".format(path),
             'a', encoding='utf-8')
for i in range(100) :
    file1.write(r"{}".format(add_str))
    file1.write('\n')
file1.close()
