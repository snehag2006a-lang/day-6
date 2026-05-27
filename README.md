# day-6
Exploratory Data Analysis 
Assignment Details
Course: Python with Data Analysis
Topic: Exploratory Data Analysis (EDA)
Dataset: WineQT.csv
Student Name: G.Sneha
Assignment No: 2
Date: May 2026
Introduction
Exploratory Data Analysis (EDA) is the process of analyzing datasets to understand their structure, patterns, relationships, and anomalies before applying machine learning models.
EDA helps in:
Understanding data distribution
Finding missing values
Detecting outliers
Identifying relationships between variables
Improving data quality
Objective
The objectives of this assignment are:
To explore WineQT dataset
To understand data structure and features
To perform data cleaning
To analyze data using visualizations
To identify relationships between variables
Dataset Information
Dataset Name: WineQT.csv
Total Rows: 1143
Total Columns: 13
Type: Structured dataset
Target Variable: Quality
Libraries Used
Pandas → Data handling
NumPy → Numerical operations
Matplotlib → Data visualization
Seaborn → Statistical plots
Warnings → Ignore unnecessary alerts
Program – Data Loading
Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr

wr.filterwarnings('ignore')

df = pd.read_csv("WineQT.csv")

print(df.head())
Data Inspection
Used functions:
df.shape → size of dataset
df.info() → data types & null values
df.describe() → statistical summary
df.columns → column names
Data Cleaning
Checked missing values using df.isnull().sum()
Checked duplicates using df.duplicated().sum()
Ensured dataset is clean before analysis
Univariate Analysis
Used:
Bar plot (Quality distribution)
Histogram (Feature distribution)
Swarm plot (Outliers detection)
Observation:
Most wines belong to medium quality range
Some features show skewed distribution
Bivariate Analysis
Used:
Pairplot
Violin plot (Alcohol vs Quality)
Box plot
Observation:
Alcohol content influences wine quality
Higher alcohol → better quality trend
Multivariate Analysis
Used:
Correlation Heatmap
Observation:
Positive correlation: variables move together
Negative correlation: variables move opposite
Some features strongly impact wine quality
Key Findings
Dataset has no major missing values
Alcohol is an important feature for quality
Some outliers exist in data
Correlation helps identify important features
Advantages of EDA
Helps understand dataset easily
Improves model performance
Detects errors and missing data
Provides visual insights
Conclusion
EDA is an essential step in data analysis. It helps in understanding the dataset before applying machine learning models. WineQT dataset shows clear patterns in wine quality based on different chemical properties.
