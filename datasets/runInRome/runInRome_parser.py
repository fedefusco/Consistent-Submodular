import numpy as np
from geopy import distance
from tqdm import tqdm
import csv

'''
  This script parses the RunInRome.txt file and creates the runInRome_dataset containing the positions list, the distance and kernel matrices 
'''

def kernelization(x,a):
    return np.exp(-(x**2/(2*a)))

with open("RunInRome.csv") as file:
  csvreader = csv.reader(file)
  positions = []
  for row in csvreader:
    lat, lon = row
    positions.append((lat,lon)) 


positions = np.array(positions)


n = len(positions)

# Creation of the distance matrix
distance_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in tqdm(range(n-1)):
  for j in range(i+1,n):
    aux = distance.distance(positions[i], positions[j]).km
    distance_matrix[j][i], distance_matrix[i][j] = aux, aux
distance_matrix = np.array(distance_matrix)

# Creation of the kernel matrix
h_squared = distance_matrix.var()
kernel_matrix = kernelization(distance_matrix,h_squared) 


np.savez_compressed("./runInRome_dataset",
                    positions = positions,
                    kernel_matrix = kernel_matrix,
                    distance_matrix = distance_matrix
                    )
                    
            
