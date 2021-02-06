import numpy as np
from urllib.request import urlopen
import urllib
import pandas as pd
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel 
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator
names = ['age', 'sex', 'cp', 'trest', 'chol', 'fb', 'rest', 'thalach', 'ex', 'oldpeak', 'slope', 'ca', 'thal', 'USERS'] 
hD = pd.read_csv('data77.csv', names = names)
hD = hD.replace('?', np.nan)
model    =    BayesianModel([('age',    'trest'),    ('age',    'fb'),    ('sex',    'trest'),    ('ex', 'trest'),('trest','USERS'),('fb','USERS'),('USERS','rest'), ('USERS','thalach'), ('USERS','chol')])
model.fit(hD, estimator=MaximumLikelihoodEstimator)
from pgmpy.inference import VariableElimination
HD_infer = VariableElimination(model)
q = HD_infer.query(variables=['USERS'], evidence={'age': 37, 'sex' :0})
print(q)
