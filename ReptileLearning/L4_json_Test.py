import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
import requests
from bs4 import BeautifulSoup as bs
from bs4 import element
import csv

folder = "D:\\GitHub\\OutputData""\\"

def training_request_lyrics():
    res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
    json = res.json()
    for item in json["data"]["song"]["list"]:
        print("歌曲名：{}".format(item["name"]))
        print("专辑：{}".format(item["album"]["name"]))
        print("时长：{}秒".format(item["interval"]))
        print("链接：{}".format("https://y.qq.com/n/yqq/song/{}.html".format(item["mid"])))

if __name__ == "__main__":
    training_request_lyrics()
