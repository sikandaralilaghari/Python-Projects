import pandas as pd

df = pd.read_csv("articles.csv")
print(df.head())
df["Number of Words"] = df["Article"].apply(lambda n: len(n.split()))
print(df.head())