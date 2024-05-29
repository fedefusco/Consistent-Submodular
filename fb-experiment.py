import numpy as np
from tqdm import tqdm
import sys


# Importing the algorithms from the relative folder
sys.path.insert(0, './algorithms/')
from swapping_class import *
from sieve_class import *
from encompassing_class import *
from chasing_class import *


# Importing the dominating function
sys.path.insert(0, './functions/')
from dominating import *


'''
Influence maximization on the fb dataset
'''

# Setting the parameters of the input
k = 20 # How many elements in the solution
epsilon = 0.1 # Precision parameter


# Instantiation of the input
fb = dominating('./datasets/fb/facebook_graph.p', k)
n = fb.n

sieve = sieve_class(fb,epsilon)
swapping = swapping_class(fb)
encompassing = encompassing_class(fb)
chasing = chasing_class(fb,epsilon)
stream = [i for i in range(n)]


# Running the SIEVE-STREAMING algorithm
print('Running the SIEVE-STREAMING algorithm on the stream')

sieve_results, sieve_consistency = [], []

for e in tqdm(stream):
  sieve.insert(e)
  sieve_consistency.append(sieve.consistency)
  S = sieve.solution
  sieve_results.append(fb.value(S))


# Running the SWAPPING algorithm
print('Running the SWAPPING algorithm on the stream')

swap_results, swap_oracles, swap_consistency = [], [], []

for e in tqdm(stream):      
  swapping.insert(e)
  swap_consistency.append(swapping.consistency)
  S = swapping.solution
  swap_results.append(fb.value(S))


# Running the CHASING-LOCAL-OPT algorithm
print('Running the CHASING-LOCAL-OPT algorithm on the stream')

chasing_results, chasing_consistency = [], []

for e in tqdm(stream):
  chasing.insert(e)
  chasing_consistency.append(chasing.consistency) 
  S = chasing.solution
  chasing_results.append(fb.value(S))  
  
  
# Running the ENCOMPASSING-SET algorithm
print('Running the ENCOMPASSING-SET algorithm on the stream')

encompassing_results, encompassing_consistency = [], []

for e in tqdm(stream):
  encompassing.insert(e)
  encompassing_consistency.append(encompassing.consistency)
  S = encompassing.solution
  encompassing_results.append(fb.value(S))




# Saving the result in the /results/fb/results folder
np.savez_compressed("./results/fb/results",
                    parameters = np.array([n,k,epsilon]),
                    sieve_results = sieve_results,
                    swap_results = swap_results, 
                    chasing_results = chasing_results, 
                    encompassing_results = encompassing_results,
                    sieve_consistency = sieve_consistency, 
                    swap_consistency = swap_consistency,
                    chasing_consistency = chasing_consistency, 
                    encompassing_consistency = encompassing_consistency
                    )
                    
