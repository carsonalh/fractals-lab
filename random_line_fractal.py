import torch
import matplotlib.pyplot as plt
import numpy as np

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

points: torch.Tensor = torch.Tensor([[0, 0, 0], [1, 0, 0]]).to(device)

RANDOM = False
BULGE_RATIO = .25
K = torch.Tensor([[0, 0, 1]]).to(device)
for _ in range(18):
    points0 = points[:-1]
    points1 = points[1:]

    midpoints = (points0 + points1) / 2
    tangents = points1 - points0
    normals = torch.cross(K, tangents, dim=1)
    if RANDOM:
        directions = (torch.ones(normals.shape) > 0.5) * 2 - 1
        new_points = midpoints + BULGE_RATIO * directions * normals
    else:
        new_points = midpoints + BULGE_RATIO * normals
    points = torch.stack((points0, new_points), dim=1).reshape((2 * len(points0), 3))
    points = torch.concat((points, points1[-1].reshape((1, 3))), dim=0)

x = points[:, 0].squeeze().cpu().numpy()
y = points[:, 1].squeeze().cpu().numpy()

plt.plot(x, y)
plt.axis('equal')
plt.show()
