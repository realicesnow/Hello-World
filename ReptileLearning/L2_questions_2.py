import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
import requests
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def request_infos(url):
    res = requests.get(url)
    print(res.status_code)
    soup = bs(res.text, "html.parser")
    rows = []
    for header in soup.find_all("header", class_="entry-header"):
        a = header.find("h2", class_="entry-title").find("a")
        title = a.text.strip()
        url = a["href"].strip()
        time = header.find("time",class_="entry-date published").text.strip()
        rows.append((title, time, url))
        print(rows[-1])
    return rows

def training_request_list():
    rows = request_infos("https://spidermen.cn/")
    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=rows[0][0][:6]
    path = folder+name+".csv"
    with open(path, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_list()
