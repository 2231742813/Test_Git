# a, b, c = 1, 2, 3,
# print('%s webz  xlsx%s saf%s' % (a, b, c))


# print(0.1+0.1+0.1-0.3)
# print(int(0.1+0.1+0.1-0.3))
# from decimal import Decimal
# a = Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3')
# print(a)

# print(5+4j > 2-3j)
# print('abc' < 'xyz')
# print((3, 2) < ('a', 'b'))


# id()用它可以查看某个变量或者对象的内存地址
# a = b = 1
# print(id(a))
# print(id(b))

#
# a = True if 5 > 5 else False
# print(a)


# name = input('名字')
# print(type(name))
# print(name)
# print()


# a = "i am"
# b = "student"
# print(a,'a', b)
# print(a,"a" , b, sep="看看我有什么作用")


# a = 1
# print(id(a))
# print(id(1))
# print(id(2))
# print('--------------')
# a = 2
# print(id(a))
# print(id(1))
# print(id(2))


# # 缓冲池
# a = 1000000
# print(id(a))
# del a   # 删除变量a
# b = 1000000
# print(id(b))


list1 = ["a", "b", '123']

for char in list1:
    print(char.join("A"))