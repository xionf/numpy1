import numpy as np

us_data="./youtube_video_data/US_video_data_numbers.csv"
uk_data="./youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
np.loadtxt(us_data,delimiter=",",dtype=int)
np.loadtxt(uk_data,delimiter=",",dtype=int)
# 添加国家信息
# 构造全为0的数据
zore_data=np.zeros((us_data.shape[0])).astype(int)
ones_data=np.ones((uk_data.shape[0],1)).astype(int)
us_data=np.hstack((zore_data,us_data))
uk_data=np.hstack((ones_data,uk_data))

# 拼接两组数据
final_data=np.vstack((uk_data,us_data))
print(final_data)