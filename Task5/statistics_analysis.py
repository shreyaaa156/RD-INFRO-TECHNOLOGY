import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("transformed_data.csv")

print("First 5 Rows:")
print(df.head())


print("\nDescriptive Statistics:")
print(df.describe())


print("\nMean Salary:")
print(df['salary'].mean())


print("\nMedian Salary:")
print(df['salary'].median())


print("\nMode Age:")
print(df['age'].mode())


print("\nStandard Deviation of Salary:")
print(df['salary'].std())


numeric_df = df.select_dtypes(include=['number'])

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)


plt.figure(figsize=(8,6))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.savefig("correlation_heatmap.png")

plt.show()

print("\nStatistical Analysis Completed Successfully!")