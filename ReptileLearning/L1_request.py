import requests
import time
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def request_data(url, is_text=True):
    # url: str
    while True:
        res = requests.get(url)
        if res.status_code == 100:
            print("1秒后继续请求")
            time.sleep(1)
            continue
        elif res.status_code == 200:
            print("请求成功")
            return res.text if is_text else res.content
        else:
            print("不可访问")
            return None

def training_request_text():
    text = request_data('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP响应状态码.md')
    if text == None:
        return

    name = input("请输入保存文件名(输入为空时默认使用内容前五字.txt)：")
    if name == "":
        name=text[:6]
    path = folder+name+".txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("文件已保存到：{}".format(path))

def training_request_image():
    img = request_data('https://res.pandateacher.com/2019-01-12-15-29-33.png', is_text=False)
    if img == None:
        return

    name = input("请输入保存文件名(输入为空时默认为requested_img.jpg)：")
    if name == "":
        name="requested_img.jpg"
    if "." not in name:
        name=name+".jpg"

    path = folder+name
    with open(path, "wb") as f:
        f.write(img)
    print("文件已保存到：{}".format(path))

def training_request_audio():
    img = request_data('https://static.pandateacher.com/Over%20The%20Rainbow.mp3', is_text=False)
    if img == None:
        return

    name = input("请输入保存文件名(输入为空时默认为requested_ado.mp3)：")
    if name == "":
        name="requested_ado.mp3"
    if "." not in name:
        name=name+".mp3"

    path = folder+name
    with open(path, "wb") as f:
        f.write(img)
    print("文件已保存到：{}".format(path))

def training_request_html():
    text = request_data('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
    if text == None:
        return

    name = input("请输入保存文件名(输入为空时默认使用内容前五字.html)：")
    if name == "":
        name=text[:6]
    path = folder+name+".html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("文件已保存到：{}".format(path))

if __name__ == "__main__":
    # training_request_text()   #文字下载
    # training_request_image()  #图片下载
    # training_request_audio()  #音频下载
    training_request_html()   #网页下载
