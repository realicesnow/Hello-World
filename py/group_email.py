import smtplib
from email.mime.text import MIMEText
from email.header import Header
import Module.path_util as path
import csv_operator as csv_op

class MailMessage:
    def __init__(self, sub_type="plain", charset="utf-8"):
        self.title = ""
        self.content = ""
        self.from_header = ""
        self.to_header = ""
        self.sub_type = sub_type
        self.charset = charset

    def set_to_header(self,mail_list):
        format_list = []
        for pair in mail_list:
            format_list.append("{}<{}>".format(pair[0],pair[1]))
        print(format_list)
        self.to_header = ",".join(format_list)

    def CreateMessage(self):
        message = MIMEText(self.content, self.sub_type, self.charset)
        message['From'] = Header(self.from_header, self.charset)
        message['To'] = Header(self.to_header, self.charset)
        message['Subject'] = Header(self.title, self.charset)
        return message.as_string()

class SMTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.receivers = []

    def _create_server(self):
        pass

    def connect(self, username, password):
        try:
            self.sender = username  # 发件人地址与账户一致
            print("sender: {}".format(self.sender))
            self._create_server()
            print("login...")
            self.server.login(username, password)
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False

    def sendmail(self, message):
        try:
            self.server.sendmail(self.sender, self.receivers, message)
            return True
        except smtplib.SMTPException as e:
            print(e)
            return False

    def __del__(self):
        self.server.quit()

class GMailServer(SMTPServer):
    def __init__(self):
        SMTPServer.__init__(self, "smtp.gmail.com", "587")

    def _create_server(self):
        self.server = smtplib.SMTP(self.host, self.port)
        self.server.starttls()

class QQMailServer(SMTPServer):
    def __init__(self):
        SMTPServer.__init__(self, "smtp.qq.com", "465")

    def _create_server(self):
        self.server = smtplib.SMTP_SSL(self.host, self.port)

    def connect(self, username, password):
        key = password if password != "" else "pmabajpbcifdbjee"
        return SMTPServer.connect(self, username, key)

# 无手机接收授权码
# class Mail126Server(SMTPServer):
#     def __init__(self):
#         SMTPServer.__init__(self, "smtp.126.com", "25")

#     def _create_server(self):
#         self.server = smtplib.SMTP(self.host, self.port)
#         self.server.starttls()

class YahooJpMailServer(SMTPServer):
    def __init__(self):
        SMTPServer.__init__(self, "smtp.mail.yahoo.co.jp", "587")

    def _create_server(self):
        self.server = smtplib.SMTP(self.host, self.port)


def get_mail_list():
    while True:
        try :
            p = path.PathUtil(input("输入文件路径："))
            csv_lines = csv_op.get_csv_rows(p.get_path())
            mail_list = list()
            for item in csv_lines:
                mail_list.append((item[0], item[1]))
            return mail_list
        except Exception as e:
            print(e)

def send_mail():
    server = GMailServer()
    while True:
        username = input("输入账户：")
        password = input("输入密码：")
        if server.connect(username, password):
            break
        print("登陆失败！")
        if input("输入q退出，输入其他重新输入密码。") == "q":
            return
    
    mail_list = get_mail_list()
    print(mail_list)
    for item in mail_list:
        server.receivers.append(item[1])

    message = MailMessage()
    message.title = "Python SMTP 邮件测试"
    message.from_header = "菜鸟"
    message.set_to_header(mail_list)
    print(message.to_header)
    message.content = input("输入邮件内容：\n")

    if not server.sendmail(message.CreateMessage()):
        print("发送失败")
        return

if __name__ == "__main__":
    send_mail()
