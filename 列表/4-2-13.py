a1 = [1, 2, 33, 5, 66, 3]
print(a1)
a1.sort()
#sort是升序，降序结合reverse操作
print(a1)
#也可以定义一个函数来赋值参数key来排序
a2 = ["dfd", "er", "er0", "jkl", "hjll"]
a2.sort()
#默认根据首字母顺序排序
print(a2)
a2.sort(key=len)
#规定根据字符串长度排序
print(a2)