from igraph import *
import pickle

''' Implementation of the Dominating function'''

class dominating:
  def __init__(self, arrayFile, k):
    '''
    It's expected that arrayFile contains the pickle of the FB graph with the circles
    '''  
    
    with open(arrayFile,'rb') as file:
      self.g = pickle.load(file)

    self.n = self.g.vcount()   
    self.k = k
      
  def marginal(self,S,x):
    """Compute the marginal value of x to S"""  

    neighborhood_x = set(self.g.neighborhood(x))
    neighborhood_S = set()
    
    for s in S:
      neighborhood_S = neighborhood_S.union(set(self.g.neighborhood(s)))
        
    return len(neighborhood_x - neighborhood_S)      


  def value(self,S):
    """Compute the value of S"""
    neighborhood_S = set()

    for s in S:
      neighborhood_S = neighborhood_S.union(set(self.g.neighborhood(s)))
        
    return len(neighborhood_S)


  def feasible(self,S):
    """Feasibility oracle of S"""
    
    return len(S) <= self.k
      
      
      
      
      

