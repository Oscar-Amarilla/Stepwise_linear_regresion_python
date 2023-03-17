#This algorithm will compute a linear regression (simple or multiple) and return an 
#ANOVA table. This script is inspired by the chapters 11 and 12 of the Walpole-Meyers^2
#PROBABILITY & STATISTICS FOR ENGINEERS & SCIENTISTS 9th edition.

import numpy as np

import pandas as pd

import math

import scipy.stats

def linear_regression(A,y):

#Creating I_n, an array of "n" ones.
    i = pd.DataFrame(np.ones(len(y)))

#Concatenating I_n and A
    X = pd.concat([i,A], axis=1)

#Initializin a list with the regressors.
    regressors = list(X)

#A little of linear algebra.
    B = (X.T).dot(X)

    B_inv = pd.DataFrame(np.linalg.inv(B))

    XTy = (X.T).dot(y)

#The array b is contains all the coefficients, including b_0.
    b = B_inv.dot(XTy.values)

#Getting the total number of parameters (b_0 + regressors).
    tot_param = len(b)

#Getting the number of observations.
    n = len(y)

#Computing the predictions.
    y_hat = X.dot(b.values)

#Computing the mean of the observations.
    y_bar = y.mean()

#Taking the principal diagonal of the variance-covariance matrix.
    cov = pd.Series(np.diag(B_inv), index=[B_inv.index, B_inv.columns])

#Computing the sum of square errors.
    sse = y.dot((y-y_hat)) #Sum of square errors

#Computing the sum of total squares.
    sts = y.dot(y)-n*y_bar**2

#Computing R_2 value.
    R_2 = 1-sse/sts

#Computing the adjusted R_2 value.
    R_2_adj = 1-(sse/sts)*((n-1)/(n-tot_param))

#Square residual mean.
    s_2 = sse/(n-tot_param) # sse/(n-(k+1) , Mean error.  

#Initializing the dataframe that will contain the regression and the ANOVA. 
    regression_tests = pd.DataFrame()

    for i in range(0,tot_param):
        
#Computing the standard error.
        se = math.sqrt(s_2*cov[i]) # Standar error

#Computing the t-value.
        t = b[i]/se

#Computing the p-value.
        p = scipy.stats.t.sf(abs(t), df=n-tot_param)*2

#Adding the b_0 term to the ANOVA.
        if i == 0:

            dict_aux = {"Regressor": "b_0", "Coeff": b[i], "Standard Error": se, "t-statistic": abs(t), "p-value": round(p,4), "R^2": 0, "R_2 adjusted": 0}

        else:

            dict_aux = {"Regressor": regressors[i], "Coeff": b[i], "Standard Error": se, "t-statistic": abs(t), "p-value": round(p,4), "R^2": R_2, "R_2 adjusted": R_2_adj}

        regression_tests= regression_tests.append(dict_aux, ignore_index=True)

#Rounding the values to 4 decimals.
    regression = regression_tests.round(4)

    return regression 
