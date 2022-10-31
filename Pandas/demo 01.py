import pandas as pd

# numpy能够帮助我们处理数值，但pandas处理处理数值之外，还能够帮我们处理其他数据
# Series 一维，带标签的数组
t=pd.Series([1,2,3,4,5,6])
print(t)
print(("\n"))
t1=pd.Series([1,2,3,4,5,6],index=list("abcdef"))
print(t1)
print("\n")
# 通过字典创建
dict={"name":"xiaoming","age":"30"}
t2=pd.Series(dict)
print(t2)
print(t2.index)
print(t2.values)

# DataFrame