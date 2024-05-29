from sortedcontainers import SortedSet  #https://grantjenks.com/docs/sortedcontainers/sortedset.html

class swapping_class:
    ''' this class maintains a solution for swapping '''


    def __init__(self,submInstance):
    
        self.solution = set() # the solution maintained by the algorithm
        self.sorted_solution = SortedSet()  # a sorted set that contains the elements in the solutions in the form (w_e,e)
        self.consistency = 0 # the consistency counter
        self.submInstance = submInstance
            
    def insert(self, e):
        ''' Insert element e '''
        S = self.solution.copy()
        w_e = self.submInstance.marginal(S,e)
        
        s_e, w_s_e = self.find_swapping(e, w_e)
        if s_e == set() or w_s_e * 2 <= w_e:
            self.consistency += 1  
            self.solution.add(e)
            self.sorted_solution.add((w_e, e))
            
            if s_e != set():
                self.solution.discard(s_e)
                self.sorted_solution.discard((w_s_e,s_e))
     
        return
    

    def find_swapping(self, e, w_e):
        ''' find the element s_e, returns an (empyset, zero), if e + S is feasible in O(1) running time '''

        submInstance = self.submInstance
        if submInstance.feasible(self.solution.union({e})):
            return (set(),0)
        
        w_s_e, s_e = self.sorted_solution[0]

        return s_e, w_s_e
                
      
        
        
        
        
        
        
        
        
        
        
        
        
        
