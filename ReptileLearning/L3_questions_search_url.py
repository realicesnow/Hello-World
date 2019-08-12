import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
from py.Module.rs_data import request_data as rs_data
from bs4 import BeautifulSoup as bs
from bs4 import element
from urllib.parse import quote
import csv
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def training_request_search_urls(name):
    search_url = "http://s.ygdy8.com/plus/so.php?typeid=1&keyword={}".format(quote(name.encode("gbk")))
    text = rs_data(search_url)
    soup = bs(text, "html.parser")
    urls = []
    for item in soup.find("div", class_="co_content8").find_all("table"):
        try :
            sub_url = item.find("b").find("a")["href"].strip()
            urls.append("http://s.ygdy8.com{}".format(sub_url))
        except Exception as e:
            print(e)
            continue
    return urls

def training_request_download_url(url):
    text = rs_data(url, encode="gbk")
    soup = bs(text, "html.parser")
    name = soup.find("div", class_="bd3r").find("div", class_="title_all").text.strip()
    a = soup.find("div", class_="co_content8").find("div", id="Zoom").find("a")["href"].strip()
    print( name, url )
    return (name, url)

def training_request_search_movies():
    movie_name = input("输入搜索电影名：")
    search_urls = training_request_search_urls(movie_name)
    print(search_urls)
    infos = []
    for url in search_urls:
        infos.append(training_request_download_url(url))

    name = input("请输入保存文件名(输入为空时默认使用内容前五字.csv)：")
    if name == "":
        name=infos[0][0][:5]
    path = folder+name+".csv"
    with open(path, "a", newline='', encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerows(infos)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    training_request_search_movies()
