import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
from py.Module.rs_data import request_data as rs_data
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def analyze_with_bs(text):
    soup = bs(text, "html.parser")
    tag_ul = soup.find("ul", class_="nav nav-list")
    tag_li = tag_ul.find("li")
    tags_li = tag_li.find_all("li")
    rows = []
    for li in tags_li:
        rows.append( (li.find("a").text.strip(),) )
    return rows

def training_request_categories():
    text = rs_data("http://books.toscrape.com/")
    if text == None:
        return None

    rows = analyze_with_bs(text)
    print("共计{}类".format(len(rows)))
    print(rows)
    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=text[:6]
    path = folder+name+".csv"
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_categories()
