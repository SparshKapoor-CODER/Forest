import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Forest_Loss_ML_Dataset.csv')
print("✅ Dataset loaded successfully.")

# Display basic information about the dataset
print("\nDataset Info:")
print(df.info())

# Display first few rows of the dataset
print("\nFirst 5 rows of the dataset:")
print(df.head())