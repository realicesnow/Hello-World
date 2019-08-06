import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
import requests
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def training_request_list_div():
    home_url = "http://www.xiachufang.com"
    week_url = home_url+"/explore/"
    res = requests.get(week_url)
    print(res.status_code)
    soup = bs(res.text,"html.parser")
    tag_names = soup.find_all("p", class_="name")
    tag_ellipsis = soup.find_all("p", class_="ing ellipsis")
    if len(tag_names) != len(tag_ellipsis):
        print("长度不一致")
        return None
    count = 0
    rows = []
    while count < len(tag_names):
        name_a = tag_names[count].find("a")
        name = name_a.text.strip()
        url = home_url+name_a["href"]
        ellipsis = tag_ellipsis[count].text.strip()
        rows.append((name.strip(), ellipsis, url))
        print(rows[-1])
        count += 1
    return rows

def training_request_list():
    home_url = "http://www.xiachufang.com"
    week_url = home_url+"/explore/"
    res = requests.get(week_url)
    print(res.status_code)
    soup = bs(res.text,"html.parser")
    tag_foods = soup.find_all("div", class_="info pure-u")
    rows = []
    for tag_food in tag_foods:
        name_a = tag_food.find("p", class_="name").find("a")
        name = name_a.text
        url = home_url+name_a["href"]
        # ellipsis=[]
        # for ns in tag_food.find("p", class_="ing ellipsis").children:
        #     # print(ns)
        #     e_name = ns.string.strip("、 , \n")
        #     if e_name == "":
        #         continue
        #     ellipsis.append(e_name)
        # rows.append((name.strip(), ",".join(ellipsis), url))
        ellipsis = tag_food.find("p", class_="ing ellipsis").text.strip() ## text 获取p之下的所有文本
        rows.append((name.strip(), ellipsis, url))
        print(rows[-1])
    return rows

def training_request_foods():
    rows = training_request_list()
    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=rows[0][0][:5]
    path = folder+name+".csv"
    with open(path, "w", newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_foods()
