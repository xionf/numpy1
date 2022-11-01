import numpy as np
import pandas as pd

obj = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
obj=obj.drop("c")
print(obj)

obj=obj.drop(['b','a'])
print(obj)