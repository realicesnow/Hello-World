import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
from py.Module.rs_data import request_data as rs_data
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def iterative_find_li(result_set, rows):
    for item in result_set:
        li_items = item.find_all("li")
        for li_item in li_items:
            art_item = li_item.find("article")
            footer = art_item.find("footer")
            div_author = footer.find("div", class_="comment-author vcard")
            author = div_author.find("b")
            div_time = footer.find("div", class_="comment-metadata")
            time = div_time.find("time")
            div_content = art_item.find("div", class_="comment-content")
            content = div_content.find("p")
            rows.append( ( author.text, time.text.strip("\n\t"), content.text ) )
            ol_items = li_item.find_all("ol")
            iterative_find_li(ol_items, rows)

def analyze_with_bs( text ):
    soup = bs(text, "html.parser")
    ol_items = soup.find_all("ol", class_="comment-list")
    rows = []
    iterative_find_li(ol_items, rows)
    for row in rows:
        print(row)
    return rows


def training_request_html():
    text = rs_data('https://wordpress-edu-3autumn.localprod.forc.work/all-about-the-future_04/')
    if text == None:
        return

    rows = analyze_with_bs(text)
    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=text[:6]
    path = folder+name+".csv"
    with open(path, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_html()   #网页下载
