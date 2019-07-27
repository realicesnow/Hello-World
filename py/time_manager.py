from Module.InputValue import input_value
import time
import datetime
import msvcrt
import threading
# import sys
# import tty
# import termios // linux
import locale
locale.setlocale(locale.LC_CTYPE, 'chinese')  # 显示中文时间


class InputThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.input = None
        self.quit = "N"

    def run(self):
        while self.quit != "Y":
            self.input = msvcrt.getch()

        print("input_thread is over")

    def key(self):
        return self.input

    def reset(self):
        self.input = None

    def quit_input(self):
        self.quit = "Y"
        print("{0:*^20}".format("按任意键继续"))
# linux
# def readchar():
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch


# def readkey(getchar_fn=None):
#     getchar = getchar_fn or readchar
#     c1 = getchar()
#     if ord(c1) != 0x1b:
#         return c1
#     c2 = getchar()
#     if ord(c2) != 0x5b:
#         return c1
#     c3 = getchar()
#     return chr(0x10 + ord(c3) - 65)


class Timer:
    def __init__(self):
        self.stt_time = time.time()

    def cost_sec(self):
        return time.time()-self.stt_time


def get_current_time():
    return time.strftime('[%Y年%m月%d日 %H时%M分%S秒]', time.localtime(time.time()))


def count_down_sec(task_time):
    input_th = InputThread()
    input_th.setDaemon(True)
    input_th.start()
    is_complete = False
    for i in range(task_time, -1, -1):
        timer_str = "倒计时{}秒--输入q结束".format(i)
        print(timer_str, end="")
        print("\b"*len(timer_str)*2, end="", flush=True)
        time.sleep(1)
        if input_th.key() == b"q":
            break
        input_th.reset()
    else:
        is_complete = True

    input_th.quit_input()
    input_th.join()
    return is_complete

def format_line(head, content):
    return "{0:<6}{1}".format(head, content)

def write_time_log( file_name, task_name, task_sec, cost_sec ):
    with open( file_name, "a", encoding="utf-8" ) as file:
        task_time_str = datetime.timedelta(seconds=task_sec)
        cost_time_str = datetime.timedelta(seconds=cost_sec)
        task_line = format_line("预计时长：", task_time_str)
        cost_line = format_line("实际时长：", cost_time_str)

        print(task_line)
        print(cost_line)

        file.write("{0:*^20}\n".format("任务："+task_name))
        file.write("{}\n".format(task_line))
        file.write("{}\n".format(cost_line))

def time_manager():
    input("欢迎使用“时间管理器”！请按回车继续。")
    while True:
        task_name = input('请输入任务名：')
        task_time = input_value('你觉得自己至少可以专注这个任务多少分钟？输入 N 分钟', error_msg="请输入数字")
        print("{0:*^20}\n我要完成的任务：{1}\n我至少要专注：{2}分钟\n".format(
            "此次任务信息", task_name, task_time ))

        print(get_current_time())
        timer = Timer()
        is_complete = count_down_sec(task_time*60)
        print("恭喜你完成任务！") if is_complete else print("很遗憾，你未完成任务。。。")

        if (input("是否记录？是：输入y，否：输入其他") == "y"):
            write_time_log("time_log.txt", task_name, task_time*60, timer.cost_sec())
        
        if (input("是否退出时间日志记录器？是：输入y，否：输入其他") == "y"):
            break

    print('愿被你善待的时光，予你美好的回赠。')

if __name__ == "__main__":
    time_manager()
