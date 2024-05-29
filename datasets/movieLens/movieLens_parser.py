import numpy as np
import pandas as pd
import io
from tqdm import tqdm
from scipy.sparse.linalg import svds
from scipy.linalg import svd
import sklearn.cluster
from sklearn.decomposition import TruncatedSVD
import pandas as pd

'''
This script parses the movieLens dataset and creates the movies and users feature vectors 
'''


svd_rank = 30


#Import ratings dataframe
ratings_df = pd.read_table('ratings.dat', sep='::', header=None, engine='python', encoding='ISO-8859-1', names = ['UserID', 'MovieID', 'Rating', 'Timestamp'])
ratings_df['MovieID'] = ratings_df['MovieID'].apply(pd.to_numeric)

#Import movies dataframe
movies_df = pd.read_table('movies.dat', sep='::', header=None, engine='python', encoding='ISO-8859-1', names = ['MovieID', 'Title', 'Genres'])
movies_df['MovieID'] = movies_df['MovieID'].apply(pd.to_numeric)
movies_df = movies_df.set_index('MovieID')

#Remove all the movies not rated
rated_movies = set(ratings_df['MovieID'])
all_movies = set(movies_df.index)
not_rated_movies = all_movies - rated_movies
movies_df = movies_df.drop(not_rated_movies)



#Creation of the ratings matrix
R_df = ratings_df.pivot(index = 'UserID', columns ='MovieID', values = 'Rating')
R_df = R_df.apply(lambda row: row.fillna(row.mean()), axis=1) #Completing the missing values with row-averages
R = R_df.to_numpy()


#Completion of the ratings matrix with SVD

user_ratings_mean = np.mean(R, axis = 1)
R_demeaned = R - user_ratings_mean.reshape(-1, 1) #Centering of the matrix
tsvd = TruncatedSVD(svd_rank, algorithm="arpack")
U = tsvd.fit_transform(R_demeaned)  
Vt = tsvd.components_  
completed_matrix = np.matmul(U,Vt) + user_ratings_mean.reshape(-1, 1) #This is the Completed matrix

# Extracting the feature vectors
tsvd = TruncatedSVD(svd_rank, algorithm="arpack")
users_features = tsvd.fit_transform(completed_matrix)  # users features
movies_features = tsvd.components_.T  # movies features


print(users_features.shape)
print(movies_features.shape)


np.savez_compressed("./movieLens_dataset",
                    users_features=users_features,
                    movies_features=movies_features)

