import torch
import matplotlib.pyplot as plt

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

ITERATIONS = 100
ZOOMED = True

if ZOOMED:
    re = -0.618321484624953
    im = -0.46529110341576707
    width = 0.04400693669561717
    x_values = torch.linspace(re - width / 2, re + width / 2, 2_000)
    y_values = torch.linspace(im - width / 2, im + width / 2, 2_000)
    x, y = torch.meshgrid(x_values, y_values)

else:
    points = torch.linspace(-2, 2, 2_000)
    x, y = torch.meshgrid(points, points)

c = torch.complex(x, y).to(device)
z = torch.zeros_like(c).to(device)
n = torch.zeros_like(x).to(device)

for _ in range(ITERATIONS):
    z = z * z + c
    n += torch.abs(z) > 2

plt.imshow(n.t().flip((0,)).cpu().numpy(), cmap='gnuplot')
plt.show()

