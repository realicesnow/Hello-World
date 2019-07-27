import math

def estimated( option, size, value ) :
    if option == 1 :
        number = math.ceil(size * 80 / value)
        print('项目大小为{0:.1f}个标准项目，如果需要在{1:.1f}个工时完成，则需要人力数量为：{2:d}人'.format(size,value,number))  
    elif option == 2 :
        time = size * 80 / value
        print('项目大小为{0:.1f}个标准项目，使用{1:d}个人力完成，则需要工时数量为：{2:.1f}个'.format(size,value,time))  
    else :
        print("计算类型错误: {}".format(option))

# option : 1-整数 2-浮点数
def input_value( option, message ) :
    while True :
        try :
            if   option == 1 : return int(input(message))
            elif option == 2 : return float(input(message))
            else             : break
        except :
            print("输入错误")
            
def main() :
    while True :
        option = input_value(1, '请选择计算类型：（1-人力计算，2-工时计算）')
        if option != 1 and option != 2 : print("输入错误") ; continue ;
        size = input_value(2, '请输入项目大小：（1代表标准大小，可以输入小数）')
        if option == 1 :
            time = input_value(2, '请输入工时数量：（请输入小数）')
            estimated(option, size, time)
        elif option == 2 :
            number = input_value(1, '请输入人力数量：（请输入整数）')
            estimated(option, size, number)
        if "Y" == input("是否结束计算？（结束输入Y，继续输入其他）") :
            break

main()


