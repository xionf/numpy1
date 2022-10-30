import numpy as np

arr=np.arange(10)
print(arr)
print(arr[1])
#切片slice(起始，终点，步长)
a=slice(2,7,2)
print(arr[a])
# 切片的第二种方法
arr2=arr[2:7:1]
print((arr[arr2]))

#多维数组使用
arr1=np.arange(15)
arr1.shape=(5,3)
print(arr1[2])
print(arr1[0:3])

#切片还可以包含省略号,省略号根据位置，表示取所有的行，列等
print("\n")
print(arr1)
print((arr1[...,2]))