The code is written in python3 and requires the following dependencies:

1) numpy
2) tqdm
3) igraph
4) matplotlib
5) geopy
6) csv
7) sys
8) pickle
9) sortedcontainers  #https://grantjenks.com/docs/sortedcontainers/sortedset.html

The simplest way to install them is to invoke the command:

pip3 install numpy tqdm ...

Description of the folders:

a) The algorithms folder contains the routines used in the experiments
b) The functions folder contains the implementation of the submodular functions used
b) The datasets folder already contains the raw dataset used in the experiments (they still need to be parsed) together with the parser.py scripts
c) The results folder is the destination of the output of the experiments and contains scripts to generate the plots

The main folder contains the actual experiments: 
  - coverage-experiment.py
  - fb-experiment.py
  - movielens-experiment.py
  - rome-kmedoid-experiment.py
  - rome-logdet-experiment.py
  - uber-kmedoid-experiment.py
  - uber-logdet-experiment.py


To reproduce the results:
   1) run the parser relative to the desired experiment in the corresponding dataset folder, it will parse the raw data in the dataset folder and create a pickle or a npz. For some datasets it may take several hours
      
   2) run the corresponding ...-experiment.py script in the main folder.
   
   3) step 2) generates a result.npz file in the corresponding result folder. To generate the relative plots just run the visualization.py script inside the corresponding folder. 


