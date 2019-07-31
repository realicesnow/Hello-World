import sys
sys.path.append("D:\\GitHub\\Hello-World\\")
from py.Module.rs_data import request_data as rs_data
#引入requests库
folder = "D:\\GitHub\\OutputData""\\"

def training_request_text():
    text = rs_data('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP响应状态码.md')
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
    img = rs_data('https://res.pandateacher.com/2019-01-12-15-29-33.png', is_text=False)
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
    img = rs_data('https://static.pandateacher.com/Over%20The%20Rainbow.mp3', is_text=False)
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
    text = rs_data('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
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
