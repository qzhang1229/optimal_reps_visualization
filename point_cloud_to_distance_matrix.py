''' 

Takes in a text file of point cloud of 2 dimension. Write a new text file that represents the distance matrix of the point cloud.
Author: Qingru Zhang

'''
import math
import sys
from cv2 import sqrt




def getDistance(i_coord,j_coord):
    dist = 0
    for i in range(len(i_coord)):
        dist += pow(i_coord[i] - j_coord[i],2)
    return math.sqrt(dist)

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

list_of_lists = []

file_name = sys.argv[1]
output_name = sys.argv[2]
is_transpose_str = sys.argv[3]
is_comma_str = sys.argv[4]

with open(file_name) as f:
    if is_comma_str == "true":
        for line in f:
                inner_list = [float(elt.strip()) for elt in line.split(',')]
                list_of_lists.append(inner_list)
    else:
        for line in f:
                inner_list = [float(elt.strip()) for elt in line.split('\t')]
                list_of_lists.append(inner_list)


if (is_transpose_str == "true"):
    list_of_lists = transposeMatrix(list_of_lists)

length = len(list_of_lists[0])
dimension = len(list_of_lists)

distance_matrix = []

for i in range(length):
    row = []
    point_i_coord = []
    for dim in range(dimension):
        x_i = list_of_lists[dim][i]
        point_i_coord.append(x_i)

    for j in range(length):
        point_j_coord = []
        for dim in range(dimension):
            x_j = list_of_lists[dim][j]
            point_j_coord.append(x_j)

        distance = getDistance(point_i_coord,point_j_coord)
        
        row.append(distance)
    distance_matrix.append(row)



write_file = open(output_name, "w")
for ele in distance_matrix:
    for i in range(len(ele)):
        if (i == len(ele) -1):
            write_file.write(str(ele[i]))
        else:
            write_file.write(str(ele[i]) + " ")
    write_file.write("\n")

write_file.close()





