import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Sample dataset (since you don't have file)
df = sns.load_dataset('iris')

print(df.head())
print(df.shape)
print(df.info())
print(df.describe().T)

print(df.isnull().sum())
print(df.duplicated().sum())

# Univariate analysis
sns.countplot(x='species', data=df)
plt.show()

df.hist(figsize=(8,6))
plt.show()

# Bivariate analysis
sns.pairplot(df)
plt.show()

# Multivariate analysis
plt.figure(figsize=(8,5))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()