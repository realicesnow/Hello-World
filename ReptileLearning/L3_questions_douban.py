import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
from py.Module.rs_data import request_data as rs_data
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def analyze_text(text):
    soup = bs(text,"html.parser")
    rows = []
    for item in soup.find_all("div", class_="item"):
        tag_pic = item.find("div", class_="pic")
        number = tag_pic.find("em").text.strip()
        name = tag_pic.find("a").find("img")["alt"]
        url = tag_pic.find("a")["href"]
        bd_tag = item.find("div", class_="bd")
        rating = bd_tag.find("span", class_="rating_num").text.strip()
        quote_tag = bd_tag.find("p", class_="quote")
        quote = quote_tag.text.strip() if quote_tag != None else ""
        rows.append((number, name, rating, quote, url))
        print(rows[-1])
    return rows

def training_request_list():
    home_url = "https://movie.douban.com/top250"
    sub_url_format = "?start={}&filter="
    rows_list = []
    for i in range(10):
        url = home_url+sub_url_format.format(i*25)
        text = rs_data(url)
        if text == None:
            continue
        rows_list.append(analyze_text(text))
    return rows_list

def training_request_movies():
    rows_list = training_request_list()
    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=rows_list[0][0][0][:5]
    path = folder+name+".csv"
    with open(path, "a", newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(("序号","电影名","评分","评语","链接"))
        for rows in rows_list:
            writer.writerows(rows)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_movies()
