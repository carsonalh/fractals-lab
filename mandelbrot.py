import torch
import numpy as np
import matplotlib.pyplot as plt
import sys

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

x, y = None, None
iterations = None

if len(sys.argv) <= 1:
    y, x = np.mgrid[-1.3:1.3:0.005, -2:1:0.005]
    iterations = 1_000
elif sys.argv[1] == 'zoomin':
    CENTER_X = 0.044401390345897934
    CENTER_Y = -1.3493269980029505
    WIDTH = 0.007587548048614279
    step = WIDTH / 600
    iterations = 10_000

    y, x = np.mgrid[(CENTER_X - WIDTH / 2):(CENTER_X + WIDTH / 2):step, (CENTER_Y - WIDTH / 2):(CENTER_Y + WIDTH / 2):step]

assert x is not None
assert y is not None
assert iterations is not None

x, y = torch.Tensor(x), torch.Tensor(y)

c = torch.complex(x, y).to(device)
z = torch.zeros_like(c).to(device)

n = torch.zeros_like(x).to(device)

for _ in range(iterations):
    z = z * z + c
    n += torch.abs(z) < 4.0

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

plt.imshow(processFractal(n.cpu().numpy()))
plt.show()
