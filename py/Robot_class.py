import time

class Robot:
    __id = 9527
    def __init__(self):
        print("{0:*^20}".format("编号{}机器人正在启动。请稍等。".format(self.__id)))
        for i in range(20) :
            time.sleep(0.2)
            print("--", end="")
        print("\n已启动！")
        self.name = input("请为我命名：")
    def hello(self):
        self.your_name = input("你好,我是{},请问您怎么称呼？\n".format(self.name))
    def ask_wish(self):
        self.wish = input("请问你有什么愿望？\n")
    def say_wish(self):
        print("{}的愿望是:".format(self.your_name))
        for i in range(3):
            print(self.wish)
        print("重要的事情说三遍！")


rob = Robot()
rob.hello()
rob.ask_wish()
rob.say_wish()