# optimal_reps_visualization

This repository creates a visualization to the result of the optimal representatives in python. It works together with [a rust repository that optimize cycle representatives](https://github.com/UDATG/optimal_reps). In addition, it provides some helper functions, including converting a point cloud to a distance matrix and visualizing a simplex barcode. To run the program, you need to install python and some other supporting libraries. We will go through some instructions for installing these things first.

## Install Python

Go to https://www.python.org/downloads/release/python-3104/. Choose a correct version of installer to download. Then, use the installer to install python on your computer. Now we need to add python to the system variable of your computer. You can do that by choosing to do so in the installation process. There is a check box that asks you whether you'd like to add it to the PATH. Check the box and it will automatically add python to the list of system variables. Even if you forget to check the box, you can still do that by following this instruction https://datatofish.com/add-python-to-windows-path/ for Windows or this instruction  https://www.educative.io/edpresso/how-to-add-python-to-the-path-variable-in-mac for Mac. 

## Install NumPy, matplotlib and opencv

In this repository, we uses these three libraries to do some computation and visualization. To install NumPy, open a terminal and run the following command: `pip install numpy`. To install matplotlib, use the command `pip install matplotlib`. To install opencv, use the command `pip install opencv-python`.

## Convert a point cloud to a distance matrix

In order to convert a point cloud into a distance matrix, we can use the python script point_cloud_to_distance_matrix.py. To run the file, open a terminal and run the following command: `python point_cloud_to_distance_matrix.py [input file name] [output file name] [need_transpose] [separate_by_comma]`. There are four parameters in this command. The first two are straightforward, you need to provide the input and output file name (including extension, such as .txt). The third parameter need_transpose means to tell the program whether we need to transpose the input point cloud matrix. In this program, the point cloud should place the coordinates of a point in the same column. If your input place the coordinates of a point in the same row, you need to put "true" for [need_transpose]. Otherwise, put "false" for it. The fourth parameter is separate_by_comma. It's similar to the third parameter. If your input point cloud is separated by comma, put "true" for [separate_by_comma]. Otherwise, put "false" for it.

## Visualize the simplex barcode

In order to visualize the simplex barcode, we need to have the .npy files that record the birth time and death time of the persistent homology. These .npy files should be the result of running the rust program called simplex_bar_record.rs of [this repository](https://github.com/UDATG/optimal_reps). To visualize the simplex barcode, we need to run simplex_barcode_visualization.py. To run the program, open a terminal and use the command `python simplex_barcode_visualization.py [birth time] [death time]`. There are two parameters. We need to provide the file path of the .npy files that contains the birth time and death time so that the program can open them and plot the barcode.

## Visualize the optimized cycle representative

In order to visualize the optimized cycle representative, we need to use the command `python optimized_cycle_visualization.py [point cloud file] [optimized cycle vertices npy file] [need_transpose] [separate_by_comma]`. This command is similar to the command that convert a point cloud to a distance matrix. We need to provide the point cloud, whether we need to transpose it and whether it's separated by comma. Same as the program that converts the point cloud to the distance matrix, we expect to see the coordinates of a point placed in a column, instead of a row. If the point cloud place the coordinates of a point in a row, put "true" for the parameter [need_transpose]. Similarly, put "true" for the parameter [separate_by_comma] if the point cloud is separated by comma. 

The only difference is on the second parameter [optimized cycle vertices npy file]. This should be contained in the result of running wrapper_gurobi.rs of [this repository](https://github.com/UDATG/optimal_reps). We need to provide the path of this npy file so that the program and open it and visualize the cycle representative. 


