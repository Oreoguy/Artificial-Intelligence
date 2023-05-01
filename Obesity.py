import pandas as pd
import skfuzzy as KMeans
import numpy as np

# load the dataset
df = pd.read_csv("D:\AI\Codes AI\ObesityDataSet_raw_and_data_sinthetic (2)\ObesityDataSet_raw_and_data_sinthetic.csv", encoding='unicode_escape')

# drop the last column (class label)
df.drop(df.columns[-1], axis=1, inplace=True)

# convert text data to numeric using one-hot-encoding
df = pd.get_dummies(df)

# check for missing values and drop any rows with missing values
if df.isnull().values.any():
    df.dropna(inplace=True)

# perform fuzzy k-means clustering with 7 clusters
kmeans = KMeans(n_clusters=7, init='random', fuzzy=True)
kmeans.fit(df)

# get the maximum belongingness for each sample and note the cluster
clusters = np.argmax(kmeans.fuzzy_labels_, axis=1)

# create a matrix with rows denoting cluster numbers and columns denoting weight type values
matrix = np.zeros((7,7))

# fill in the matrix with the number of samples that have maximum belongingness to a particular cluster
# and also have a label with a particular weight type
for i in range(len(clusters)):
    row = clusters[i]
    col = np.where(df.iloc[i,-7:].values == 1)[0][0]
    matrix[row][col] += 1

# print the matrix
print(matrix)
