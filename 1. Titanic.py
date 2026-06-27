import numpy as np 
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

train_data = pd.read_csv("./train.csv") # localização do arquivo
train_data.head()

test_data = pd.read_csv("./test.csv") # localização do aquivo
test_data.head()

