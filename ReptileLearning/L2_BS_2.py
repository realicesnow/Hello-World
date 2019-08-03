import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
from py.Module.rs_data import request_data as rs_data
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

# 返回名字和分页链接
def request_categories(url):
    text = rs_data(url)
    if text == None:
        return None

    soup = bs(text, "html.parser")
    tag_ul = soup.find("ul", class_="nav nav-list")
    tag_li = tag_ul.find("li")
    tags_li = tag_li.find_all("li")
    rows = []
    for li in tags_li:
        tag_a = li.find("a")
        name = tag_a.text.strip()
        link = url+tag_a["href"]
        print(name, link)
        rows.append( (name, link) )
    return rows

''' 返回列表:
    （分类名，）
    （1   , 书名，评分，价格）
    ...
'''
def request_sub(cat_info):
    text = rs_data(cat_info[1])
    if text == None:
        return None
    rows = [(cat_info[0],)]
    count = 1
    soup = bs(text, "html.parser")
    tag_section = soup.find("div", class_="alert alert-warning").parent
    tags_li = tag_section.find("ol", class_="row").find_all("li")
    for li in tags_li:
        art = li.find("article", class_="product_pod")
        score = art.find("p")["class"][1].strip()
        name = art.find("h3").find("a")["title"].strip()
        price = art.find("div", class_="product_price").find("p", class_="price_color").text.strip()
        rows.append((count, name, score, price))
        print(count, name, score, price)
        count += 1
    return rows

def training_request_books():
    cat_rows = request_categories("http://books.toscrape.com/")
    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=cat_rows[0][0][:6]
    path = folder+name+".csv"
    with open(path, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for cat in cat_rows:
            rows = request_sub(cat)
            writer.writerows(rows)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_books()
