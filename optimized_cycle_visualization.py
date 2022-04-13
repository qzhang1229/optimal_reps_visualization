import numpy as np
import matplotlib.pyplot as plt
import math

def connect_points(x,y,p1,p2):
    x1, x2 = x[p1], x[p2]
    y1, y2 = y[p1], y[p2]
    plt.plot([x1,x2],[y1,y2],'k-')
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def calculate_area(x,y,ordered_vertices):
    area = 0
    for i in range(0,len(ordered_vertices)-1,1):
        area += x[ordered_vertices[i]]*y[ordered_vertices[i+1]] - x[ordered_vertices[i+1]]*y[ordered_vertices[i]]

    area += x[ordered_vertices[len(ordered_vertices)-1]]*y[ordered_vertices[0]]-x[ordered_vertices[0]]*y[ordered_vertices[len(ordered_vertices)-1]]

    return 0.5*abs(area)

coordinates_of_points = []

with open('point_cloud/2x100-Gamma-4.csv.txt') as f:
    for line in f:
        inner_list = [float(elt.strip()) for elt in line.split('\t')]
        coordinates_of_points.append(inner_list)

x_coordinate = coordinates_of_points[0]
y_coordinate = coordinates_of_points[1]


edges = np.load("test_example_2/uniform_tri_loss_vertices.npy")


# Make an ordered list of vertices to calculate the area.
ordered_vertices = []
current_vertex = edges[0]
current_index = 0
ordered_vertices.append(current_vertex)
while(len(ordered_vertices)<len(edges)/2):
    for i in range(0,len(edges),1):
        if (edges[i]==current_vertex and i != current_index):
            if (i % 2 == 0):
                ordered_vertices.append(edges[i+1])
                current_index = i+1
                current_vertex=edges[i+1]
            else:
                ordered_vertices.append(edges[i-1])
                current_index = i-1
                current_vertex=edges[i-1]


print(ordered_vertices)
# Sum up loss values
edge_num = 0
edge_length = 0.0
area = calculate_area(x_coordinate,y_coordinate,ordered_vertices)
for i in range (0,len(edges),2):
    edge_length+=connect_points(x_coordinate,y_coordinate,edges[i],edges[i+1])
    edge_num += 1

print("Number of edges:"+ str(edge_num))
print("Length of edges:"+ str(edge_length))
print("Area:"+ str(area))

plt.scatter(x_coordinate,y_coordinate)
plt.show()

