import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_data.csv")

print("First 5 Rows:")
print(df.head())

# Convert purchase_date into datetime format
df['purchase_date'] = pd.to_datetime(df['purchase_date'])

# Create Annual Salary column
df['annual_salary'] = df['salary'] * 12

# Create Age Group column
df['age_group'] = pd.cut(
    df['age'],
    bins=[18, 30, 45, 60],
    labels=['Young', 'Adult', 'Senior']
)

# Rename purchase_amount column
df.rename(columns={'purchase_amount': 'purchase'}, inplace=True)

print("\nTransformed Data:")
print(df.head())

# Save transformed dataset
df.to_csv("transformed_data.csv", index=False)

print("\nTransformation completed successfully!")