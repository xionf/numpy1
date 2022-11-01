import pandas as pd

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj)

# 用该Series的reindex将会根据新索引进行重排。如果某个索引值当前不存在，就引入缺失值
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
print(obj2)