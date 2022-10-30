import numpy as np
#方法1
a=np.arange(15).reshape(5,3)
print("原数组:\n",a )

#运用flat数组迭代器
for x in a.flat:
    print(x)

#利用flatten进行拷贝，不会影响原数组
print(a.flatten())
print("\n")
print(a.flatten(order="F"))

#ravel方法，也是展平，但会影响原数组