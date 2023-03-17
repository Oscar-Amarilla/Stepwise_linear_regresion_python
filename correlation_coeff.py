'''This algorithm computes the correlation coeficient between the vectors x and y.'''

import pandas as pd

import numpy as np

def r_coeff(x,y):

#Initializing a vector of n ones.
    i = pd.DataFrame(np.ones(len(x)))
    
#Creating a 1x2 matrix with the means of x and y.
    means = pd.DataFrame([x.mean(),y.mean()]).T

#Creating a matrix of nx2 with the mean values in each column.
    mean_matrix = i.dot(means.values)

#Computing the difference between each component and the mean.
    dx = x - mean_matrix[0]

    dy = y -  mean_matrix[1]

#Computing the numerator of the r value: [x-x_bar]^T·[y-y_bar]
    num = dx.dot(dy)

#Computing the numerator: ||x-x_bar||·||y-y_bar||
    den = np.linalg.norm(dx)*np.linalg.norm(dy)

#Computing r.
    r = num/den

    return r

