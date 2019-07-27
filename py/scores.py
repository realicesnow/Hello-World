local_path = r"py\Data""\\"
scores_file = "scores.txt"
file1 = open(r'{}{}'.format(local_path, scores_file),'r',encoding='utf-8-sig') 
file_lines = file1.readlines()      
file1.close()

scores_list = []
for line in file_lines :
    data = line.split()
    sum = 0
    for s in data[1:] :
        sum += float(s)
    print(data[0], sum)
    scores_list.append("{} {}\n".format(data[0], sum))


with open(r"{}{}".format(local_path,"sum_scores.txt"), "w", encoding="utf-8-sig") as file2 :
    file2.writelines(scores_list)

# with open(r"{}{}".format(local_path, "sum_scores_for.txt"), "w", encoding="utf-8-sig") as file3:
#     for line in scores_list:
#         file3.write(line)

dict_scores = {}
list_scores = []
final_scores = []

with open(r"{}{}".format(local_path,"sum_scores.txt"), "r", encoding="utf-8-sig") as file_r :
    list_scores = file_r.readlines()
    print(list_scores)
    for item in list_scores:
        tem_list = item.split()
        print(tem_list)
        dict_scores[tem_list[0]] = float(tem_list[1])
print(dict_scores)
sorted_list = sorted(dict_scores.items(), key=lambda x:x[1], reverse=True)
print(sorted_list)
for pair in sorted_list:
    final_scores.append("{} {}\n".format(pair[0],pair[1]))
print(final_scores)
with open(r"{}{}".format(local_path,"sorted_scores.txt"), "w", encoding="utf-8-sig") as file_w :
    file_w.writelines(final_scores)