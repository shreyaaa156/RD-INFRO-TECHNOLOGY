import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Show missing values before cleaning
print("Missing Values Before Cleaning:\n")
print(df.isnull().sum())

# Fill numerical columns with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Purchase_Amount'] = df['Purchase_Amount'].fillna(df['Purchase_Amount'].mean())

# Fill categorical columns with mode
df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
df['City'] = df['City'].fillna(df['City'].mode()[0])
df['Is_Member'] = df['Is_Member'].fillna(df['Is_Member'].mode()[0])

# Fill missing dates
df['Purchase_Date'] = df['Purchase_Date'].fillna(df['Purchase_Date'].mode()[0])

# Show missing values after cleaning
print("\nMissing Values After Cleaning:\n")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates()

# Check again
print("Duplicates After Removal:", df.duplicated().sum())

# Clean column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.lower()

print("\nCleaned Column Names:\n")
print(df.columns)

# Save cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned dataset saved successfully!")