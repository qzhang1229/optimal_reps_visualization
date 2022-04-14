# optimal_reps_visualization

This repository creates a visualization to the result of the optimal representatives in python. In addition, it provides some helper functions, including converting a point cloud to a distance matrix and visualizing a simplex barcode. To run the program, you need to install python and some other supporting libraries. We will go through some instructions for installing these things first.

## Install Python

Go to https://www.python.org/downloads/release/python-3104/. Choose a correct version of installer to download. Then, use the installer to install python on your computer. Now we need to add python to the system variable of your computer. You can do that by choosing to do so in the installation process. There is a check box that asks you whether you'd like to add it to the PATH. Check the box and it will automatically add python to the list of system variables. Even if you forget to check the box, you can still do that by following this instruction https://datatofish.com/add-python-to-windows-path/ for Windows or this instruction  https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac for Mac. 

## Install NumPy, matplotlib and opencv

In this repository, we uses these three libraries to do some computation and visualization. To install NumPy, open a terminal and run the following command: `pip install numpy`. To install matplotlib, use the command `pip install matplotlib`. To install opencv, use the command `pip install opencv-python`.

## Convert a point cloud to a distance matrix

In order to convert a point cloud into a distance matrix, we can use the python script point_cloud_to_distance_matrix.py. To run the file, open a terminal and run the following command: `python point_cloud_to_distance_matrix.py [input file name] [output file name] [need_transpose] [separate_by_comma]`. There are four parameters in this command. The first two are straightforward, you need to provide the input and output file name (including extension, such as .txt). The third parameter need_transpose means to tell the program whether we need to transpose the input point cloud matrix. In this program, the point cloud should place the coordinates of a point in the same column. If your input place the coordinates of a point in the same row, you need to put "true" for [need_transpose]. Otherwise, put "false" for it. The fourth parameter is separate_by_comma. It's similar to the third parameter. If your input point cloud is separated by comma, put "true" for [separate_by_comma]. Otherwise, put "false" for it.

## Visualize the simplex barcode

In order to visualize the simplex barcode, you need to have the .npy files that record the birth time and death time of the persistent homology. These .npy files should be the result of running simplex_bar_record.rs of [this repository](https://github.com/UDATG/optimal_reps).
