import pandas as pd
import numpy  as np

a=pd.DataFrame(np.arange(15).reshape(3,5),columns=list("abcde"))
print(a)

a.loc[:,"e"]=a.loc[:,"c"]-a.loc[:,"a"]
print(a)