import numpy as np
from numpy import nan

# nan不是一个数，两个nan不相等
print(np.nan==np.nan)
print(np.nan!=np.nan)

# 判断数组中nan 的个数
arr=np.array([1,2,4, nan,67, nan])
print(np.count_nonzero(arr!=arr))

# 通过函数判断是否是nan
arr[np.isnan(arr)]=0
print(arr)

#