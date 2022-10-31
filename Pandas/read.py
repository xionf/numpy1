import pandas as pd
from pymongo import MongoClient
# 读取外部数据
a=pd.read_csv("../youtube_video_data/USvideos.csv")
print(a)
# 