from MyQR import myqr
import os
import requests
from io import BytesIO
from pyzbar import pyzbar
from PIL import Image, ImageEnhance
from path_util import PathUtil

def decode_QR(img_adds):
    """ 读取二维码的内容： img_adds：二维码地址（可以是网址也可是本地地址 """
    if os.path.isfile(img_adds):
        # 从本地加载二维码图片
        img = Image.open(img_adds)
    else:
        # 从网络下载并加载二维码图片
        rq_img = requests.get(img_adds).content
        img = Image.open(BytesIO(rq_img))
    # img.show()  # 显示图片，测试用
    txt_list = pyzbar.decode(img)
    decoded_texts=[]
    for txt in txt_list:
        decoded_texts.append(txt.data.decode("utf-8"))
    return decoded_texts

def encode_QR(words, picture=None, colorized=True, save_name="", save_dir="" ):
    if picture != None :
        picture = picture.strip('''"'"''')
        pair = os.path.split(picture)
        if "." not in pair[1]:
            print("错误的文件名！")
            return
        picture_full_name = pair[1].split(".")
        name = picture_full_name[0]
        extension = picture_full_name[1]
        if save_name == "":
            save_name = name + "_toQR"
        if "." not in save_name and len(extension) != 0:
            save_name += "." + extension
    
    print("保存文件名为：{}".format(save_name))
    save_dir = save_dir if save_dir != "" else os.getcwd()
    print("保存地址为：{}".format(save_dir))
    myqr.run(words, picture=picture, colorized=colorized, save_name=save_name, save_dir=save_dir )
    path = PathUtil(save_dir+'\\'+save_name)
    print("生成QR图片已保存到：{}".format(path.get_path()))

def read_qrcode():
    qr_add = input("输入QR图片地址：")
    qr_add = qr_add.strip('''"'"''')
    if os.path.isfile(qr_add):
        path = PathUtil(qr_add)
        qr_add = path.get_path()
    
    print("正在解码。。。")
    return decode_QR(qr_add)

def create_qrcode(text):
    print("{0:*^30}".format("准备生成二维码"))
    picture = input("输入图片地址：")
    save_name = input("输入保存图片名称(输入为空时默认使用图片名称+toQR)：")
    save_dir = input("输入保存图片地址(输入为空时使用当前路径)：")
    print("开始生成QR图片。。。")
    encode_QR(words=text, picture=picture, save_name=save_name, save_dir=save_dir)

def reset_qrcode():
    decoded_texts = read_qrcode()
    for text in decoded_texts:
        print(text)
        create_qrcode(text)

if __name__ == '__main__':
    # text = input("输入二维码内容：")
    # create_qrcode(text)
    reset_qrcode()