# 由于系统原因，这里修改后的test.txt不会即时显示变化，你需要重新打开文件-root下的test.txt。
# 或者在本地新建文件夹，复制test.txt，在本地运行这段代码。
from Module.InputValue import input_value
from Module.path_util import PathUtil
from Module.disp_util import disp

encode = "utf-8-sig"

def input_row(input_msg, len):
    return input_value(input_msg, "请输入0-{}之间的数数字".format(len-1), ran=(0, len-1))

def modify_file(path):
    with open (path,'r', encoding=encode) as f:
        lines = f.readlines()
        print(lines)
    while True:
        disp(lines)
        modify_row = input_row("请选择要修改的行数：",len(lines))
        modified_str = input("请输入第{}行要替换的内容：".format(modify_row))
        lines[modify_row] = modified_str.rstrip("\n") + "\n"
        ask_exit = input("是否结束修改并保存文件？(结束：Y，继续：其他)")
        if ask_exit == "Y":
            with open(path, "w", encoding=encode) as file:
                file.writelines(lines)
            break

if __name__ == "__main__":
    path = PathUtil("py\Data\gushi.txt")
    modify_file(path.get_path())