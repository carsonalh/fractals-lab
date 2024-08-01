import torch
import numpy as np
import matplotlib.pyplot as plt

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

X, Y = np.mgrid[-2:2:0.005, -2:2:0.005]

x = torch.Tensor(X)
y = torch.Tensor(Y)

x = x.to(device)
y = y.to(device)

z = torch.exp(-(x**2 + y**2) / 2.0)

plt.imshow(z.cpu().numpy())
plt.tight_layout()
plt.show()

