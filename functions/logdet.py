from math import log
import numpy as np

''' Implementation of the log det function'''

class logdet:
    def __init__(self, arrayFile, k, alpha):
      '''
      It's expected that the arrayFile is an .npz file containing:
      '''      
      
      npzdata = np.load(arrayFile, allow_pickle=False)
      # Initialization of the features and cluster vectors
      
      self.pos = npzdata['positions']
      self.kernel = npzdata['kernel_matrix']

      # Initialization of parameters
      self.n = self.pos.shape[0] # Number of points
      self.k = k 
      self.alpha = alpha # Perturbation parameter to have the adjusted kernel matrix positive definite
      
      
    def marginal(self,S,x):
      """Compute the marginal value of x to S"""
      
      SUx = set(S).union({x})
      return self.value(SUx) - self.value(S)


    def value(self,S):
      """Compute the value of S"""
      
      S_list = sorted(list(S))
      aux = np.eye(len(S_list)) + self.alpha * self.kernel[np.ix_(S_list,S_list)]
      sign, val = np.linalg.slogdet(aux)
      return val
      

    def feasible(self,S):
      """Feasibility oracle of S"""
      
      return len(S) <= self.k



      
      
       





