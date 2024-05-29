from math import ceil, floor, log, sqrt
from sortedcontainers import SortedSet  #https://grantjenks.com/docs/sortedcontainers/sortedset.html

class chasing_class:
    ''' this class maintains a solution for CHASING-LOCAL-OPT algorithm '''

    def __init__(self,submInstance, eps):
        self.solution = set() # Current solution
        self.arrived = set()  # Elements arrived so far
        self.sorted_arrived = SortedSet() # Elements arrived so far sorted according to the current marginal to the solution
        self.submInstance = submInstance
        
        self.eps = eps # Precision parameter
        self.consistency = 0
        self.phi = ( 1 + sqrt(5) ) / 2
        self.N = ceil((log(12/eps, self.phi))/eps) 

    def recompute_sorted_arrived(self,S):
      '''This function recomputes the sorted_arrived
      sorted set after each change in the solution, so to
      compute efficiently the candidate element to insert'''
      
      submInstance = self.submInstance
      self.sorted_arrived = SortedSet()
      for v in self.arrived:
        self.sorted_arrived.add((submInstance.marginal(S,v),v))
      return 
      
    def candidate(self,S):
      ''' this function finds the candidate to swap out in S'''
      
      submInstance = self.submInstance
      phi, k = self.phi, submInstance.k
      fS = submInstance.value(S)
      
      (fv, v) = self.sorted_arrived[-1]
      if fv >= phi/k * fS:
          return v
      return -1 # if the element with largest marginal contribution fails the test, then return -1
    
    def min_swap(self,S,x):
      ''' this function swaps x into S removing the element with smallest marginal contribution'''
      
      submInstance = self.submInstance
      k = submInstance.k
      
      if submInstance.feasible(S.union({x})):
        return S.union({x})
        
      value_best_swap, best_swap = 0, 0
      
      #Find the element s in S with smallest f(s|S - r)
      for r in S:
        aux_value = submInstance.value(S.union({x}) - {r})
        if  aux_value >= value_best_swap:
          best_swap, value_best_swap = r, aux_value
          
      return S.union({x}) - {best_swap}
    

    def insert(self, e):
        ''' Insert element e '''
        
        submInstance = self.submInstance
        old_solution = self.solution.copy()
        
        self.arrived.add(e)
        self.sorted_arrived.add((submInstance.marginal(old_solution, e),e))
        
        phi, k = self.phi, submInstance.k
        S = self.solution.copy()
        N = self.N
        
        # Consider the inserted element e for insertion in the solution (add it directly if it fits in k)
        if submInstance.value(S.union({e})) >= (phi/k + 1) * submInstance.value(S) or submInstance.feasible(S.union({e})):
          S = self.min_swap(S,e)
          self.recompute_sorted_arrived(S)
          
        while N >= 0: # Extra local swaps
          N-=1
          v = self.candidate(S)
          if v == -1:
            break # no element arrived so far clears the value condition 
          S = self.min_swap(S,v)
          self.recompute_sorted_arrived(S)

        self.solution = S.copy()
        
        self.consistency += len(S - old_solution)
        return
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
