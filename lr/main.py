
from sklearn.cluster import KMeans
from sklearn.svm import SVC
import numpy as np
import plotly.graph_objects as go


def get_z(x_coord, y_coord):
    return (-svc.intercept_[0] - svc.coef_[0][0] * x_coord - svc.coef_[0][1] * y_coord) / svc.coef_[0][2]


range_min = 0
range_max = 200
points_count = 50
point_size = 5

x = np.random.randint(range_min, range_max, points_count)
y = np.random.randint(range_min, range_max, points_count)
z = np.random.randint(range_min, range_max, points_count)

points = [[x[i], y[i], z[i]] for i in range(points_count)]

clusters = KMeans(2).fit(points).labels_

colors = ['red' if clusters[i] == 1 else 'blue' for i in range(points_count)]

svc = SVC(kernel='linear')
svc.fit(points, clusters)

space = np.linspace(range_min, range_max)
x_x, y_x = np.meshgrid(space, space)

fig = go.Figure()
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color=colors, size=point_size)))
fig.add_trace(go.Surface(x=x_x, y=y_x, z=get_z(x_x, y_x)))
fig.show()

