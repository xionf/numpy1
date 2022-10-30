import numpy as np
# 三元运算符
a=np.arange(15).reshape(5,3)
# 把a中小于10的数字替换为2，大于10的替换为15
a=np.where(a<=10,2,14)
print(a)

# 把小于10的替换成10，大于18的替换成18
b=np.arange(25).reshape(5,5)
b=b.clip(10,18)
print(b)