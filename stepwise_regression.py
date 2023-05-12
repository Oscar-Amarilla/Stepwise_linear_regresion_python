#This algorithm will compute a linear regression (simple or multiple) and return an 
#ANOVA table. This script is inspired by the chapters 11 and 12 of the Walpole-Meyers^2
#PROBABILITY & STATISTICS FOR ENGINEERS & SCIENTISTS 9th edition.

import pandas as pd
import numpy as np
from typing import Tuple, Union
from linear_regression import LinearRegression
import warnings
import math
import scipy.stats
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

class StepwiseRegression:

    def __init__(self) -> None:
        self.regressors = None
        self.coeff = None
        self.bias = None
        self.anova_report = None

    def fit(self, A:pd.DataFrame, y:pd.Series) -> Tuple[pd.DataFrame, pd.DataFrame]:
    #Taking the regressors.
        columns = A.columns.to_list()

    #Getting the number of regressors.
        n_features = A.shape[1]

    #Initilizing the list that will contain the regressors with best t-statistic values.
        best_t = []

    #Initializing a dataframe that will contain an ANOVA summary of the process.
        self.anova_report = pd.DataFrame()

    #Importing the linear regression operator.
        lr = LinearRegression()

    #By default, itarate n times.
        for i in range(n_features):

    #Initializing an auxiliar dataframe.
            aux = pd.DataFrame()

    #Going through each column.
            for column in columns:

    #Concatenate a particular column with the others columns related to the
    #regressors with highest t-value. The 'appear' function is a trigger that
    #returns the first argument when conditions are satisfied.
                if i == 0:
                    data = A[column]
                else:
                    data = A[[column]+best_t]

    #Computing the regression.
                lr.fit(data, y)

    #Saving the regression output.
                aux = aux.append(lr.anova_report.iloc[1:], ignore_index=True)

    #Sorting the regressions outputs with respect to the t-value.
            output = aux.sort_values(by="t-statistic", ascending=False).reset_index(drop=True)

    #Dropping from the regressors already taken by the method.
            for feature in best_t:
                output = output.loc[output["Regressor"]!=feature].reset_index(drop=True)

    #If the p-value is greater than 0.05, means regressors leaft are statistically insignigicant, so, the process stops.  
            if output["p-value"].iloc[0] > 0.05:
                return self
    # Updating the anova report.
            self.anova_report = self.anova_report.append(output.iloc[0], ignore_index=True)

    #Taking the regressor with the highest t-statistic value.
            regressor = output["Regressor"][0]
            best_t.append(regressor)
    #Getting the coefficients (b_o + features) of the best current model.
            lr.fit(A[best_t],y)
            self.coeff = lr.coeff
            self.bias = lr.bias
            self.regressors = best_t

    #Dropping the last regressor taken in order to not include it in the 
    #next iteration.
            columns.remove(regressor)

    #If there is no regressor left, stop the process.
            if len(columns) == 0:
                return self

    def predict(self,X:Union[np.ndarray,pd.DataFrame]) -> np.array:
        y_hat = np.dot(X,self.coeff) + self.bias
        return y_hat   
