import pandas as pd
import numpy as np



#read data from 'test.csv' and 'train.csv'

test_data = pd.read_csv("test.csv")
train_data = pd.read_csv("train.csv")


#preview the first 5 lines of test_data and train_data
print(test_data.head())
print(train_data.head())

