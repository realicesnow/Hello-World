import csv
import Module.path_util as path
from Module.InputValue import input_value
import chardet


def print_rows(rows):
    for idx, val in enumerate(rows):
        print("{0:<3}{1}".format(idx, val))


def get_encoding(path):
    with open(path, 'rb') as f:
        return chardet.detect(f.read())['encoding']

def get_csv_rows(path):
    encode = get_encoding(path)
    print(encode)
    with open(path, newline='', encoding=encode) as f:
        # 参数encoding = 'utf-8'防止出现乱码
        reader = csv.reader(f)
        rows = list(reader)
        return rows


def del_csv_row(path):
    rows = get_csv_rows(path)
    while True:
        print_rows(rows)
        row = input_value(
            "输入删除的行数：", error_msg="请输入0-{}之间的数数字".format(len-1), ran=(0, len(rows)-1))
        del rows[row]
        if "Y" == input("结束：Y，继续：其他"):
            break
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    p = path.PathUtil(r"D:\Python\py\Data\test.csv")
    # del_csv_row(p.create_path("product.csv"))
    print_rows(get_csv_rows(p.create_path("product.csv")))

    # with open(p.create_path("product.csv"), 'a', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['4', '猫砂', '25', '1022', '886'])
    #     writer.writerow(['5', '猫罐头', '18', '2234', '3121'])
    # print_rows(get_csv_rows(p.create_path("product.csv")))
