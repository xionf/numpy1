import numpy as np

t=np.arange(24).reshape(4,6)
print(t)
print("\n")
# 求每一列的和
t1=t.sum(axis=0)
print(t1)
print("\n")
# 求每一行的均值
t1=t.mean(axis=1)
print(t1)
print("\n")
 
#中值：median()；最大值：max();最小值：min();极值：ptp();标准差：std()