# % 格式化：str % ()
print('%s%d' % ('数字：', 0))
print('%d，%d' % (0, 1))
print('%d，%d，%d' % (0, 1, 0))

name1 = 'Python'
print('I am learning %s' % name1)  # 注：当只跟一个数据时，%后可不加括号，format()一定要有。

# format()格式化函数：str.format()
print('\n{}{}'.format('数字：', 0))  # 优势1：不用担心用错类型码。
print('{}，{}'.format(0, 1))  # 不设置指定位置时，默认按顺序对应。
print('{1}，{0}'.format(0, 1))  # 优势2：当设置指定位置时，按指定的对应。
print('{0}，{1}，{0}'.format(0, 1))  # 优势3：可多次调用format后的数据。

name2 = 'Python基础语法'
print('我正在学{}'.format(name2))  # format()函数也接受通过参数传入数据。
