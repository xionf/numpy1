#整数数组索引
import numpy as np
arr=np.array([[1,2],[3,4],[5,6]])
#取位置为（0,1） 和 （2,0）的元素
print(arr[[0,2],[1,0]])

#获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：' )
print (x)
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]])
y = x[rows,cols]
print  ('这个数组的四个角元素是：')
print (y)

#bool索引
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print ('我们的数组是：')
print (x)
print ('\n')
# 现在我们会打印出大于 5 的元素
print  ('大于 5 的元素是：')
print (x[x >  5])

# ~（取补运算符）来过滤 非复数
a = np.array([1+2j,4+2j, 3])
print(a[~np.iscomplex(a)])
