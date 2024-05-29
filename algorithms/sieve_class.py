from random import choice
import heapq
from math import ceil, floor, log

class sieve_class:
    ''' this class maintains a solution according to the Sieve Algorithm '''

    def __init__(self,submInstance,epsilon):
        self.solution = set()
        self.submInstance = submInstance
        self.epsilon = epsilon
        self.consistency = 0
        self.m = 0.01
        self.active_solutions = {}
    
    def insert(self, e):
        ''' Insert element e '''
        submInstance = self.submInstance
        k = submInstance.k
        epsilon = self.epsilon
        self.m = max(self.m, submInstance.value({e}))
        old_solution = self.solution.copy()
        for i in range(ceil(log(self.m,1+epsilon)), floor(log(2*k*self.m, 1+epsilon))):
            v = (1+epsilon)**i
            S_v = self.active_solutions.get(i,set())
            if k > len(S_v) and submInstance.marginal(S_v,e) >= (v/2 - submInstance.value(S_v))/(k-len(S_v)):
                S_v = S_v.union({e})
            self.active_solutions[i] = S_v
            if submInstance.value(S_v) >= submInstance.value(self.solution):
                self.solution = S_v.copy()
        self.consistency += len(self.solution.difference(old_solution))
        
        return
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
