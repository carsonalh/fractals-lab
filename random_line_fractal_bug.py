import matplotlib.pyplot as plt
import numpy as np

x0 = np.array([0, 0, 0])
x1 = np.array([1, 0, 0])
points = [x0, x1]

a = np.vstack((x0, x1))
x = a[:, 0]
y = a[:, 1]

fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot(x, y)
fig.canvas.draw()
fig.canvas.flush_events()

#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()

K = np.array([0, 0, 1])
for _ in range(19):
    newpoints = []
    for x0, x1 in zip(points, points[1:]):
        xm = (x0 + x1) / 2
        direction = (x1 - x0) / 4
        xnew = x0 + np.cross(K, direction)
        newpoints.append(x0)
        newpoints.append(xnew)
    newpoints.append(points[-1])
    #a = np.vstack(newpoints)
    #x = a[:, 0]
    #y = a[:, 1]
    #line.set_xdata(x)
    #line.set_ydata(y)
    #fig.canvas.draw()
    #fig.canvas.flush_events()
    points = newpoints

a = np.vstack(points)
x = a[:, 0]
y = a[:, 1]

plt.plot(x, y)
plt.show()

#print(points)
