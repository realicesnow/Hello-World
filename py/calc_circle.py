import sys
import math

def input_value(input_msg, error_msg=None, is_int=True, ran=(1, 0)):
    while True:
        try:
            value = int(input(input_msg)) if is_int else float(input(input_msg))
            if ran[0] > ran[1]:
                return value
            if value < ran[0] or value > ran[1]:
                raise Exception()
            return value
        except Exception:
            if error_msg != None:
                print(error_msg)
# 如流程图所示，求圆的面积和周长的代码
# 圆周率(pi)取3.14即可
def calc_circle():
    print("{0:*^30}".format("计算圆的面积与周长"))
    radius = input_value("输入半径：", is_int=False, ran=(0, sys.float_info.max), error_msg="输入错误，请重新输入。")
    print("面积为：{}".format(math.pi*math.pow(radius,2)))
    print("周长为：{}".format(2*math.pi*radius))

if __name__ == "__main__":
    calc_circle()