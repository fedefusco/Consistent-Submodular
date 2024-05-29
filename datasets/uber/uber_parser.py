from math import log, ceil, floor
from random import choice, sample, seed
from geopy import distance
import heapq
import numpy as np
from random import *
from tqdm import tqdm
from igraph import *
import pickle
import csv

'''
This script parses the uber dataset uber-raw-data-apr14.csv, samples 2% of it and creates the distance and kernel matrix
'''
p = 1/50

seed(0)

def kernelization(x,a):
    return np.exp(-(x**2/(2*a)))
  

with open('uber-raw-data-apr14.csv') as file:

  csvreader = csv.reader(file)
  header = next(csvreader)
  data = []
  for row in csvreader:
      data.append(row)


positions = []

for point in tqdm(data):
  if random() < p:
    date, lat, lon, base = point
    if (float(lat), float(lon)) not in positions: #Removes duplicates
      positions.append((float(lat), float(lon)))

positions.sort()
n = len(positions)

# Creation of the distance matrix
distance_matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in tqdm(range(n-1)):
  for j in range(i+1, n):
    aux = distance.distance(positions[i], positions[j]).km
    distance_matrix[j][i], distance_matrix[i][j] = aux, aux
distance_matrix = np.array(distance_matrix)


# Creation of the kernel matrix
h_squared = 5000
kernel_matrix = kernelization(distance_matrix,h_squared)


np.savez_compressed("./uber_dataset",
                    positions = positions,
                    distance_matrix = distance_matrix,
                    kernel_matrix = kernel_matrix
                    )





