import numpy as np

class kmedoid:
    def __init__(self, arrayFile, e_0, k):
      '''
      It's expected that the arrayFile is an .npz file containing:
      positions and distances.
      '''      
      
      npzdata = np.load(arrayFile, allow_pickle=False)
      # Initialization of the features and cluster vectors
      
      self.pos = npzdata['positions']
      self.distance = npzdata['distance_matrix']

      # Initialization of parameters
      self.n = self.pos.shape[0] # Number of points
      self.k = k  # Number of acceptable points
      self.e_0 = e_0
      self.f_e_0 = sum(self.distance[e_0])

    def marginal(self,S,x):
      """Compute the marginal value of x to S"""
      
      SUx = S.union({x})
      return self.value(SUx) - self.value(S)

    def value(self,S):
      """Compute the value of S"""
      
      S_list = sorted(list(S.union({self.e_0})))
      val = sum(np.amin(self.distance[S_list,:], axis = 0))
      return (self.f_e_0 - val)/self.n
          

    def feasible(self,S):
      """Feasibility oracle of S"""
      return len(S) <= self.k








