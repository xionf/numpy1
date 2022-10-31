from matplotlib import pyplot as plt

x=range(2,16,2)
y=[15,15,14,111,13,131,151]
# 设置图片大小和模糊程度
plt.figure(figsize=(10,8),dpi=120)
# 绘图
plt.plot(x,y)
# 设置x轴的刻度,精度为0.5
a=[i/2 for i in range(4,32)]
# plt.xticks(a)
plt.xticks(a[::3])

# 保存
# plt.savefig("./1.png")
# 展示
plt.show()