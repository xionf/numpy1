import numpy as np
#numpy.transpose 函数用于对换数组的维度
a = np.arange(12).reshape(3, 4)
print('原数组：')
print(a)
print('\n')
print('对换数组：')
print(np.transpose(a))


# numpy.rollaxis 函数向后滚动特定的轴到一个特定位置
# 格式：numpy.rollaxis(arr, axis, start)

# numpy.swapaxes 函数用于交换数组的两个轴
# 格式：numpy.swapaxes(arr, axis1, axis2)