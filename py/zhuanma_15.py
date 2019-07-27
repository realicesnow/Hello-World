# 1.分别使用gbk和utf-8编码自己的名字，并将其打印出来。
name = input("输入名字：")
en_gbk = name.encode("gbk")
print(en_gbk)
en_utf8 = name.encode("utf-8")
print(en_utf8)

# 2.复制上一步得到的结果，进行解码，打印出你的名字（两次）。
print(en_gbk.decode("gbk"))
print(en_utf8.decode("utf-8"))

# 3.使用gbk解码：b'\xb7\xe7\xb1\xe4\xbf\xc6\xbc\xbc\xd3\xd0\xd2\xe2\xcb\xbc'，并打印出来。
print(b'\xb7\xe7\xb1\xe4\xbf\xc6\xbc\xbc\xd3\xd0\xd2\xe2\xcb\xbc'.decode("gbk"))