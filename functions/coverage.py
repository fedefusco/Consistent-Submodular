from igraph import *
import pickle

''' Dominating'''

class coverage:
  def __init__(self, i, k, delta):
    '''
    It's expected that arrayFile contains the pickle of the FB graph with the circles
    '''  
    self.k = k
    self.i = i
    self.delta = delta
    self.n = (self.k+1) * (self.i+1) - 1
    self.oracle_calls = 0
    self.stream = []
    for j in range(i+1):
      for ell in range(k):
        self.stream += [{(j,ell)}]
      if j != i:
        self.stream += [{(j,ell) for ell in range(k)}]
  def marginal(self,S,x):
    """Compute the marginal value of x to S"""  
    return self.value(S.union({x})) - self.value(S)

  def value(self,S):
    """Compute the value of S"""
    self.oracle_calls += 1
    covered_elements = set()
    for s in S:
      covered_elements = covered_elements.union(self.stream[s])
    aux = 0
    for (j,x) in covered_elements:
      if j < self.i:
        aux += 2**j
      else: aux += 2**self.i - self.delta
    return aux


  def feasible(self,S):
    """Feasibility oracle of S"""
    return len(S) <= self.k
      
      
      
      
      

