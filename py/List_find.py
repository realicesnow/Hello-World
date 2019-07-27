scores = [91, 95, 97, 99, 92, 93, 96, 98]

average = sum(scores)/len(scores)
print("平均分为：{0:-^10.2f}".format(average))

print("{0:<10}".format("方法1："))
for i in scores:
    if i < average:
        print("{0:3}".format(i), end=" ")
print("\n")

print("{0:<10}".format("方法2："))


def FindFirstGreater(value, scores):
    for inx, val in enumerate(scores):
        if val > value:
            return inx
    return 0


def PrintLessThan(value, scores):
    temp = scores.copy()
    temp.sort()
    index = FindFirstGreater(value, temp)
    print(temp[:index])


PrintLessThan(average, scores)

print("{0:<10}".format("方法3："))


def GetLessThan(value, scores):
    return [i for i in scores if i < value]


print(GetLessThan(average, scores))
