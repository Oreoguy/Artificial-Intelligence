import pandas as pd
import skfuzzy as fuzz
import numpy as np


df= pd.read_csv('Obesityfun.csv')
# df1 = pd.get_dummies(df['family_history_with_overweight'])
# df = pd.concat([df,df1],axis=1).reindex(df.index)

#df.drop('family_history_with_overweight',axis=1,inplace=True)
df.head()