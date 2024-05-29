import numpy as np

''' Implementation of the MovieLens function'''

class movieLens:
    def __init__(self, arrayFile, alpha, k, user_features):
      '''
      It's expected that the arrayFile is an .npz file containing:
      users and movies features.
      '''      
      
      npzdata = np.load(arrayFile, allow_pickle=False)
      # Initialization of the features and cluster vectors
      self.uf = npzdata['users_features']
      self.mf = npzdata['movies_features']
      
      # Initialization of parameters
      self.n = self.mf.shape[0] # Number of movies
      self.u = self.uf.shape[0] # Number of users
      self.alpha = alpha
      self.k = k  # cardinality
      
      # Preprocessing for the marginal valuation
      self.mm = self.mf.dot(self.mf.T) # Matrix of the scalar product between movies
      self.compatibilities = np.array([max(user.dot(user_features),0) for user in self.uf]) # Scalar product of each user feature vector against the base user


    def marginal(self,S,x):
      """Compute the marginal value of x to S"""
      
      additive_term = self.compatibilities[x] # Additive term
      nearest_neighbours = [max([self.mm[i][j] for j in S], default=0) for i in range(self.n)] # Associate each movie with the best movie in S
      covering_term = sum([max(self.mm[x][i] - nearest_neighbours[i],0) for i in range(self.n)]) # Computation of the covering term
      return self.alpha * covering_term + (1 - self.alpha) * additive_term

    def value(self,S):
      """Compute the value of S"""
      
      additive_term = sum([self.compatibilities[x] for x in S]) # Additive term
      covering_term = sum([max([self.mm[i][j] for j in S], default=0) for i in range(self.n)]) # Computation of the covering term
      return self.alpha * covering_term + (1 - self.alpha) * additive_term

    def feasible(self,S):
      """Feasibility oracle of S"""
      
      return len(S) <= self.k
    

