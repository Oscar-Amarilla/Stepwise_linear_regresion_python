# [Stepwise_linear_regresion_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python)

by Oscar Amarilla, 2023

[Stepwise_linear_regresion_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python) allow python users to apply stepwise linear regression. Stepwise linear regression is an statistical technique used to downscale the number of features needed to get an optimal linear model for regression based on the statistical singnificance of each of them.

The user is free to copy, modify, and distribute this proyect, even for commercial purposes, without asking for permission. See *[Public domain dedication](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python#public-domain-dedication)* for details.

## How does [Stepwise_linear_regresion_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python) works?

The project emulates the functionality of the scikit-learn packages using ".fit" and ".predict" instaces. There are two main functions in this project: LinerRegression, which performs a traditional linear regression, and StepwiseRegression, that does the most interesting part. 

The structure of the project is the following:

```
|--linear_regression.py (Performs a linear regression)
|
|--stepwise_regression.py (Performs the stepwise regression)
|
|__ requirements.txt (List of libraries used to develop this project and versions of each one)
|
|__ README.md 
```

The aplication example jupyter notebook will help the user to know what is the project about.

## How to run [Stepwise_linear_regresion_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python)?

The user may want to check for the requirements in the requirements.txt file to know with which 
libraries the project was developed and avoid inconsistencies. If there is a problem with the user enviorment and the project dependencies, the following instructions must be followed to make it work. 

After cloning the repository, create a virtual enviornment in the same folder

```bash
python -m venv name_of_the_venv # The name of the venv is up to the user.
```
Activate the virtual enviorment

```bash
source name_of_the_venv/bin/activate
```
Then install the requirements listed in the requirements.txt using pip.

```bash
pip install -r requirements.txt
```
Finally, the notebook can be executed.

```bash
jupyter notebook
```
## Future work

The stepwise regression model depends on the linear regression method, this linear regression method is based purelly in linear algebra. The next step is to change it for a gradient descent approach in order to return better linear models. 

## References 

<ul>
    <li>Strang, (2006). Linear Algebra and its Applications (4th ed.), Chapter 3, Cengage Learning.</li>
    <li>Walpole, Meyers,Meyers (2016). Probability and Statistics for Engineers and Scientist (9th ed.), Chapter 11 and 12, Pearson. </li>
</ul>

## Contributing to [Stepwise_linear_regresion_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python)

Every comment and/or suggestion for improving [Stepwise_linear_regresion_python](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python) will be very wellcome, so every user is coordially invated to [open an issue or pull request on GitHub](https://github.com/Oscar-Amarilla/Stepwise_linear_regresion_python).

## Public domain dedication

This work is dedicated to the [public domain (CC0 1.0)](https://creativecommons.org/publicdomain/zero/1.0/). To the extent possible under law, Oscar Amarilla has waived all copyright and related or neighboring rights to the README checklist. See the LICENSE file for all the legalese.