from math import ceil, floor, log

class encompassing_class:
    ''' this class maintains a solution for the ENCOMPASSING-SET algorithm '''

    def __init__(self,submInstance):
        self.solution = set() # Set containint the current solution
        self.queue_solution = [] # queue containint the current solution
        self.B_t = set() # Encompassing set
        self.submInstance = submInstance
        self.consistency = 0
        self.beta = 1.14

    def insert(self, e):
        ''' Insert element e '''
        
        submInstance = self.submInstance
        B_t = self.B_t
        old_solution = self.solution.copy()
        
        if submInstance.value(B_t.union({e})) >= (self.beta/submInstance.k + 1) * submInstance.value(B_t):
          self.B_t.add(e)
          
          if not submInstance.feasible(self.solution.union({e})):
            old_element = self.queue_solution.pop(0) # remove from the solution the oldest element
            self.solution.remove(old_element)
        
          self.solution.add(e)
          self.queue_solution.append(e)

        new_solution = self.solution
        
        self.consistency += len(new_solution - old_solution)
        
        return
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
