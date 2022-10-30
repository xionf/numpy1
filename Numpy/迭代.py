import numpy as np
#NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式
a=np.arange(15).reshape(5,3)
print ('原始数组是：')
print (a)
print ('迭代输出元素：')
for x in np.nditer(a):
    print (x, end="," )
print("\n")
b=np.arange(1,10)
print(b)
