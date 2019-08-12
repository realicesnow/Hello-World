import requests
import time
#引入requests库
def request_data(url, is_text=True, encode=None):
    # url: str
    while True:
        res = requests.get(url)
        if encode != None:
            res.encoding = encode
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