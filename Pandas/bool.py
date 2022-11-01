import numpy as np
import pandas as pd
a=np.arange(15).reshape(-1,1)
a=pd.DataFrame(a,columns=["age"])
# 且 &  或 |  
print(a[(a["age"]>10)&(a["age"]<12)])