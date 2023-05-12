#This algorithm will compute a linear regression (simple or multiple) and return an 
#ANOVA table. This script is inspired by the chapters 11 and 12 of the Walpole-Meyers^2
#PROBABILITY & STATISTICS FOR ENGINEERS & SCIENTISTS 9th edition.

import pandas as pd
import numpy as np
import math
import scipy.stats
from typing import Union
import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

class LinearRegression:

    def __init__(self) -> None:
        self.coeff = None
        self.bias = None
        self.anova_report = None
    
    def fit(self, A:pd.DataFrame, y:pd.Series) -> pd.DataFrame:
    #Creating I_n, an array of "n" ones.
        i = np.ones([y.size,1])

    #Concatenating I_n and A
        A = pd.DataFrame(A)
        X = np.concatenate((i,A), axis=1)

    #Initializing a list with the regressors.
        features = ['b_0'] + A.columns.tolist()

    #A little of linear algebra.
        X_T = np.transpose(X)
        B = np.dot(X_T,X)
        B_inv = np.linalg.inv(B)
        XTy = np.dot(X_T,y)

    #This contains all the coefficients, including b_0 (bias).
        coeff_aux = np.dot(B_inv,XTy)

    #Setting the bias.
        self.bias = coeff_aux[0]
        self.coeff = coeff_aux[1:]

    #Getting the total number of parameters (b_0 + features).
        tot_param = 1 + self.coeff.size 

    #Getting the number of samples.
        n_samples = y.size

    #Computing the predictions.
        y_hat = np.dot(X,coeff_aux)

    #Computing the mean of the observations.
        y_bar = np.mean(y)

    #Taking the principal diagonal of the variance-covariance matrix.
        varcov_diag = np.diag(B_inv)

    #Computing the sum of square errors.
        sse = np.dot(y,(y-y_hat)) #Sum of square errors

    #Computing the sum of total squares.
        sts = np.dot(y,y)-n_samples*y_bar**2

    #Computing R_2 value.
        R_2 = 1-sse/sts

    #Computing the adjusted R_2 value.
        R_2_adj = 1-(sse/sts)*((n_samples-1)/(n_samples-tot_param))

    #Square residual mean.
        s_2 = sse/(n_samples-tot_param) # sse/(n-(k+1) , Mean error.  

    #Initializing the dataframe that will contain the regression and the ANOVA. 
        regression_tests = pd.DataFrame()

        for i in range(0,tot_param):
            
    #Computing the standard error.
            se = math.sqrt(s_2*varcov_diag[i]) # Standar error

    #Computing the t-value.
            t = coeff_aux[i]/se

    #Computing the p-value.
            p = scipy.stats.t.sf(abs(t), df=n_samples-tot_param)*2

    #Adding the b_0 term to the ANOVA.
            if i == 0:

                dict_aux = {"Regressor": "b_0", "Coeff": self.bias, "Standard Error": se, "t-statistic": abs(t), "p-value": round(p,4), "R^2": 0, "R_2 adjusted": 0}

            else:

                dict_aux = {"Regressor": features[i], "Coeff": self.coeff[i-1], "Standard Error": se, "t-statistic": abs(t), "p-value": round(p,4), "R^2": R_2, "R_2 adjusted": R_2_adj}

            regression_tests= regression_tests.append(dict_aux, ignore_index=True)

    #Rounding the values to 4 decimals.
        self.anova_report = regression_tests.round(4)

        return self

    def predict(self,X:Union[np.ndarray,pd.DataFrame]) -> np.array:
        y_hat = np.dot(X,self.coeff) + self.bias
        return y_hat

