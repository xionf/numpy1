import pandas as pd
import numpy as np
# index,columns行列索引

a=pd.DataFrame(np.arange(32).reshape(8,4),index=[1,2,3,4,5,6,7,8],columns=list("abcd"))

print(a)

# dataframe传入字典
d1={"name":["xiaoming","chengyuan"],"age":[20,19],"tel":[10086,10012]}
a1=pd.DataFrame(d1)
print(a1)

# dateframe中的head方法会显示前5行，tail(2)会显示末尾2行：默认的是5行

# 相关信息预览
print(a1.info())

#快速综合统计结果：计数，均值，标准差，最大值，四分位数，最小值
print(a1.describe())

# 排序
a1=a1.sort_values(by="age",ascending="true")
print(a1)

# 索引切片-方括号写数组，表示对行进行操作，写字符串表示对列进行操作
print(a[:5]["b"])

# loc和iloc两个方法分别通过标签和位置来索引获取行数据



