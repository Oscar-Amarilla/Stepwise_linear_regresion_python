from linear_model import linear_regression

from aux_math_functions import hat, appear

import pandas as pd

import warnings

warnings.filterwarnings('ignore')

warnings.simplefilter('ignore')

def stepwise_linear_regression(A,y):

#Taking the regressors.
    columns = list(A)

#Getting the number of regressors.
    n = len(columns)

#Initilizing the list that will contain the regressors with best t-statistic values.
    best_t = columns

#Initializing a dataframe that will contain an ANOVA summary of the process.
    anova_report = pd.DataFrame()

#By default, itarate n times.
    for i in range(n):

#Initializing an auxiliar dataframe.
        aux = pd.DataFrame()

#Going through each column.
        for column in columns:

#Concatenate a particular column with the others columns related to the
#regressors with highest t-value. The appear function is a trigger that
#returns the first argument when conditions are satisfied.
            data = pd.concat([A[column], appear(A[best_t],i,1)], axis=1)

#Computing the regression.
            regression = linear_regression(data,y)

#Dropping the intersection term.
            regression = regression.drop(0)

#Saving the regression output.
            aux = aux.append(regression, ignore_index=True)

#Sorting the regressions outputs with respect to the t-value.
        output = aux.sort_values(by="t-statistic", ascending=False).reset_index(drop=True)

#Clearing the best_t list. This is done here because previously had to 
#have some content in order to use it in the line 39.
        if i == 0:

            best_t = []

#Dropping from the regressors already taken by the method.
        else:

            for x in best_t:

                output = output.loc[output["Regressor"]!=x].reset_index(drop=True)

#If the p-value is greater than 0.05, means regressors leaft are statistically insignigicant, so, the process stops.  
        if output["p-value"].iloc[0] > 0.05:

            return anova_report, linear_regression(A[best_t],y)

        anova_report = anova_report.append(output.iloc[0], ignore_index=True)

#Taking the regressor with the highest t-statistic value.
        regressor = output["Regressor"][0]

        best_t.append(regressor)

#Dropping the last regressor taken in order to not include it in the 
#next iteration.
        columns.remove(regressor)

#If there is just one regressor left, stop the process.
        if len(columns) == 0:

            return anova_report, linear_regression(A[best_t],y)
