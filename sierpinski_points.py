from typing import Sequence, Tuple
import matplotlib.pyplot as plt
import numpy as np
import random

def midpoint(p0: Tuple[float, float], p1: Tuple[float, float]) -> Tuple[float, float]:
    a = ((p1[0] - p0[0]) / 2., (p1[1] - p0[1]) / 2.)
    m = (p0[0] + a[0], p0[1] + a[1])
    return m

def sample_vertex(vertices: Sequence[Tuple[float, float]]):
    return random.sample(vertices, 1)[0]

if __name__ == '__main__':
    VERTICES = ((0., 0.), (1., 0.), (0.5, 1.))

    BEGIN_POINT = (0.5, 0.5)

    x_points = []
    y_points = []

    p = BEGIN_POINT

    for _ in range(10_000):
        random_vertex = sample_vertex(VERTICES)
        m = midpoint(p, random_vertex)

        x_points.append(m[0])
        y_points.append(m[1])

        p = m

    x_vertices = list(map(lambda p : p[0], VERTICES))
    y_vertices = list(map(lambda p : p[1], VERTICES))

    plt.scatter(x_vertices, y_vertices, c='red')

    plt.scatter(x_points, y_points, s=0.1 * np.ones_like(y_points))
    plt.show()
