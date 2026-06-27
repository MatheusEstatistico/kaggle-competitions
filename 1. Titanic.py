import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("./train.csv") # localização do arquivo
train_data.head()

test_data = pd.read_csv("./test.csv") # localização do aquivo
test_data.head()

## Análise exploratória 
women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)

print("% of women who survived:", rate_women)

men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)

print("% of men who survived:", rate_men)

