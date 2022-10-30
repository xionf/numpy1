import numpy as np
t1=np.arange(12).reshape(2,6)
t2=t1+12
# 将t1,t2,横直拼接
t3=np.vstack((t1,t2))
print(t3)
# 水平拼接
t4=np.hstack((t1,t2))
print(t4)

#数组的行列交换
t1[[0,1],:]=t1[[1,0],:]
print(t1)