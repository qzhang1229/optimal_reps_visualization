import numpy as np
import matplotlib.pyplot as plt
import math
import sys

def transposeMatrix(matrix):
    res = []
    row_length = len(matrix[0])
    col_length = len(matrix)
    for i in range (row_length):
        row = []
        for j in range(col_length):
            row.append(matrix[j][i])
        res.append(row)
    
    return res

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

point_cloud_file = sys.argv[1]
vertices_file = sys.argv[2]
is_transpose_str = sys.argv[3]
is_comma_str = sys.argv[4]
# 'point_cloud/2x100-Gamma-4.csv.txt'
with open(point_cloud_file) as f:
    if is_comma_str == "true":
        for line in f:
                inner_list = [float(elt.strip()) for elt in line.split(',')]
                coordinates_of_points.append(inner_list)
    else:
        for line in f:
                inner_list = [float(elt.strip()) for elt in line.split('\t')]
                coordinates_of_points.append(inner_list)


if (is_transpose_str == "true"):
    coordinates_of_points = transposeMatrix(coordinates_of_points)

x_coordinate = coordinates_of_points[0]
y_coordinate = coordinates_of_points[1]

# "test_example_2/uniform_tri_loss_vertices.npy"
edges = np.load(vertices_file)


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

