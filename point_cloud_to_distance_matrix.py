''' 

Takes in a text file of point cloud of 2 dimension. Write a new text file that represents the distance matrix of the point cloud.
Author: Qingru Zhang

'''
import math




def getDistance(x_i,y_i,x_j,y_j):
    x_dist = abs(x_i-x_j)
    y_dist = abs(y_i-y_j)
    dist = math.sqrt(pow(x_dist,2)+pow(y_dist,2))
    return dist

list_of_lists = []

with open('2x100-Gamma-4.csv.txt') as f:
    for line in f:
        inner_list = [float(elt.strip()) for elt in line.split('\t')]
        list_of_lists.append(inner_list)

length = len(list_of_lists[0])

distance_matrix = []

for i in range(length):
    row = []
    x_i = list_of_lists[0][i]
    y_i = list_of_lists[1][i]
    for j in range(length):
        x_j = list_of_lists[0][j]
        y_j = list_of_lists[1][j]
        distance = getDistance(x_i,y_i,x_j,y_j)
        row.append(distance)
    distance_matrix.append(row)

write_file = open("dist_mat.txt", "w")
for ele in distance_matrix:
    for i in range(len(ele)):
        if (i == len(ele) -1):
            write_file.write(str(ele[i]))
        else:
            write_file.write(str(ele[i]) + " ")
    write_file.write("\n")

write_file.close()





