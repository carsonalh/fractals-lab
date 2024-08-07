import torch
import numpy as np
import matplotlib.pyplot as plt

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

ITERATIONS = 100

c = -0.835 - 0.2321j

points = torch.linspace(-2, 2, 2_000)
x, y = torch.meshgrid(points, points, indexing='ij')

z = torch.complex(x, y).to(device)
n = torch.zeros_like(x).to(device)

for _ in range(ITERATIONS):
    z = z * z + c
    n += torch.abs(z) < 2

def processFractal(a):
    """Display an array of iteration counts as a
    colorful picture of a fractal."""
    a_cyclic = (6.28*a/20.0).reshape(list(a.shape)+[1])
    img = np.concatenate([10+20*np.cos(a_cyclic),
                          30+50*np.sin(a_cyclic),
                          155-80*np.cos(a_cyclic)], 2)
    img[a==a.max()] = 0
    a = img
    a = np.uint8(np.clip(a, 0, 255))
    return a

plt.imshow(processFractal(n.t().flip((0,)).cpu().numpy()), cmap='gnuplot')
plt.show()


