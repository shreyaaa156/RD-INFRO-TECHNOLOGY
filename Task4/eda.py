import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("whitegrid")

df = pd.read_csv("transformed_data.csv")

print(df.head())


plt.figure(figsize=(8,5))

sns.histplot(
    df['age'],
    bins=10,
    kde=True
)

plt.title("Age Distribution", fontsize=16)
plt.xlabel("Age", fontsize=12)
plt.ylabel("Count", fontsize=12)

plt.savefig("age_histogram.png")
plt.show()


plt.figure(figsize=(8,5))

sns.boxplot(x=df['salary'])

plt.title("Salary Distribution", fontsize=16)
plt.xlabel("Salary", fontsize=12)

plt.savefig("salary_boxplot.png")
plt.show()

plt.figure(figsize=(8,5))

sns.countplot(x=df['gender'])

plt.title("Gender Count", fontsize=16)
plt.xlabel("Gender", fontsize=12)
plt.ylabel("Count", fontsize=12)

plt.savefig("gender_countplot.png")
plt.show()


plt.figure(figsize=(7,7))

df['age_group'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Age Group Distribution", fontsize=16)
plt.ylabel("")

plt.savefig("agegroup_piechart.png")
plt.show()

print("EDA completed successfully!")