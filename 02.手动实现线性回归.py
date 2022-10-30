import torch
learning_rate=0.01
#准备数据
x=torch.rand([500,1])
y_true=x*3+0.8
#通过模型进行计算
w=torch.rand([1,1],requires_grad=True)
b=torch.tensor(0,dtype=float,requires_grad=True)

#通过循环，反向传播，更新参数
for i in range(500):
    y_preidict = torch.matmul(x, w)+b
    # 计算损失
    loss = (y_true - y_preidict).pow(2).mean()
    if w.grad is not None:
        w.grad.data.zero_()
    if b.grad is not None:
        b.grad.data.zero_()

    loss.backward()
    w.data=w.data - learning_rate * w.grad
    b.data = b.data - learning_rate * b.grad
    print("w,b,loss",w.item(),b.item(),loss)


