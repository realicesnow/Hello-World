import random

def select_key(keys):
    while True:
        print(keys)
        key = input("请输入你选择的类别：")
        if key not in keys:
            if "Y" == input("我无法为您推荐这个类别，更换选择：Y，返回上页：其他") :
                continue
            return None
        return key

def ask_choice():
    # 三层前提
    library = {
      "肉类":{
          "牛肉":["牛腩饭", "酱牛肉", "红烧牛肉", "孜然牛肉", "芹菜炒牛肉", "葱爆牛肉", "酒烩牛肉"],
          "猪肉":["可乐焖猪肉", "卤猪肉", "干炒猪肉丝", "猪肉炖粉条", "宫保猪肉丁", "麻辣猪肉", "猪肉丸子", "猪肉焖板栗", "家制猪肉松"],
          "鸡肉":["简易烤鸡胸条", "葱香手撕鸡", "辣子手撕鸡", "四川棒棒鸡", "川香口水鸡", "口水鸡腿", "镶翠鸡卷", "蒜苔鸡腿卷", "口水鸡" ]
      },
      "蔬菜":{
          "黄瓜":["酸黄瓜", "蒸酿黄瓜", "鸡丝腐竹黄瓜", "老醋黄瓜拌木耳", "彩蛋黄瓜卷", "三文鱼黄瓜小卷"],
          "菠菜":["菠菜炒蛋", "凉拌菠菜", "鸡蛋粉丝炒菠菜", "菠菜木耳炒蛋", "涼拌芝麻菠菜", "上汤菠菜", "枸杞菠菜", "菠菜蛋饼"],
          "白菜":["醋溜白菜", "白菜炒肉片", "酸辣白菜", "白菜炖豆腐", "白菜炖粉条", "白菜木耳炖粉丝", "自制辣白菜", "番茄扒白菜"]
      }
      }
    print("选择困难？我来帮你！")
    key_index = [None,None]
    uesr_choice = None
    while True:
        print("为您推荐以下几种：")
        if key_index[0]==None:
            key_index[0] = select_key(list(library.keys()))
            if key_index[0] == None:
                continue
            key_index[1] = None
        if key_index[1]==None:
            key_index[1] = select_key(list(library[key_index[0]].keys()))
            if key_index[1]==None:
                key_index[0]=None
                continue
        food_list = library[key_index[0]][key_index[1]]
        pc_choice = random.choice(food_list)
        print("{} 您觉得如何？".format(pc_choice))
        select = input("同意: Y, 返回上页：P，退出：Q，看看其他：其他")
        if select == "Y":
            uesr_choice = pc_choice
            break
        elif select == "P":
            key_index[1]=None
            continue
        elif select == "Q":
            break
    
    if uesr_choice != None:
        print("您的最终选择是：{}".format(uesr_choice))
        print("{0:*^30}".format("祝您用餐愉快"))
    else:
        print("很遗憾，没能帮到您。。。")

if __name__ == "__main__":
    ask_choice()
