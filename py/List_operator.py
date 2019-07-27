list1 =  [91, 95, 97, 99]  
list2 =  [92, 93, 96, 98]
list_com0 = list1 + list2
print("list1 :", list1)
print("list2 :", list2)
print("list_com0 :", list_com0)

list_com1 = list1.copy()
for i in list2 :
        list_com1.append(i)
        
print("list_com1 :", list_com1)

list_com2 = list1.copy()
list_com2.extend(list2)
print("list_com2 :", list_com2)

list_com3 = list1.copy()
list_com3[len(list_com3):len(list_com3)] = list2
list_com3.sort(reverse=True)
print("list_com3 :", list_com3)
