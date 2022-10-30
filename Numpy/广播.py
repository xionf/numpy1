# numpy 对不同形状(shape)的数组进行数值计算的方式
import numpy as np
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([0, 1, 2])
bb=np.tile(b,(4,1))
print(b)
print(a + b)