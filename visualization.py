import numpy as np
import matplotlib.pyplot as plt


def connect_points(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')

coordinates_of_points = []

with open('point_cloud/2x100-Gamma-4.csv.txt') as f:
    for line in f:
        inner_list = [float(elt.strip()) for elt in line.split('\t')]
        coordinates_of_points.append(inner_list)

x_coordinate = coordinates_of_points[0]
y_coordinate = coordinates_of_points[1]

edges = np.load("npy_files/weighted_tri_answer_vertices.npy")
print(edges)

for i in range (0,len(edges),2):
    connect_points(x_coordinate,y_coordinate,edges[i],edges[i+1])

plt.scatter(x_coordinate,y_coordinate)
plt.show()

