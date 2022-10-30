from __future__ import print_function
import torch
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
a.requires_grad_(True)
a.backward()
print(a.grad)
