import pandas as pd
df = pd.read_csv("Forest_Loss_ML_Dataset.csv")
print("✅ Dataset loaded successfully.")
df = df.drop(columns=["lossyear", ".geo", "system:index"])
print("Cleaned dataset shape:", df.shape)
print(df.head())
df.to_csv("Forest_Loss_ML_CLEAN.csv", index=False)
print("✅ Dataset cleaned and saved successfully.")