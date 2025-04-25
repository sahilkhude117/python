import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Load dataset
df = pd.read_csv("city_day.csv")

# 1. Independant and dependant variables
independent_vars = df.drop(columns=['AQI'])
dependant_vars = df['AQI']

num_independent = independent_vars.select_dtypes(include=[np.number]).shape[1]
print("Number of independent variables:", num_independent)
print("Number of dependent variables: 1 (AQI)")

# 2. Top 5 and last 5 rows
print("\nTop 5 rows:\n", df.head())
print("\nLast 5 rows:\n", df.tail())

# 3. Descriptive statistics
print("\nDescriptive statistics:\n", df.describe())

# 4. Independent variable with minimum average value
numeric_cols = df.select_dtypes(include=[np.number]).drop(columns=['AQI']).columns
min_avg_var = df[numeric_cols].mean().idxmin()
print("\nIndependent variable with minimum average value:", min_avg_var)

# 5. Independent variable with highest standard deviation
max_std_var = df[numeric_cols].std().idxmax()
print("Independent variable with highest standard deviation:", max_std_var)

# 6. Missing values in independent variables
missing_counts = df[independent_vars.columns].isnull().sum()
print("\nMissing values in independent variables:\n", missing_counts[missing_counts > 0])

# Visualize missing values (bar chart)
plt.figure(figsize=(10, 5))
missing_counts[missing_counts > 0].sort_values(ascending=False).plot(kind='bar', color='salmon')
plt.title("Missing Values in Independent Variables")
plt.xlabel("Independent Variables")
plt.ylabel("Missing Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Independent variable with max missing values
max_missing_var = missing_counts.idxmax()
print("\nIndependent variable with maximum missing values:", max_missing_var)


# 7. Replace missing values in one variable with mean (e.g., PM2.5)
if 'PM2.5' in df.columns:
    df['PM2.5'] = df['PM2.5'].fillna(df['PM2.5'].mean())
    print("\nMissing values in 'PM2.5' replaced with mean.")


# 8. Histogram of an independent variable (e.g., NO2)
plt.figure(figsize=(8, 4))
sns.histplot(df['NO2'].dropna(), bins=30, kde=True, color='skyblue')
plt.title("Histogram of NO2")
plt.xlabel("NO2")
plt.ylabel("Frequency")
plt.show()

# 9. Outliers using boxplot (e.g., PM10)
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['PM10'], color='orange')
plt.title("Boxplot of PM10 (Outlier Detection)")
plt.xlabel("PM10")
plt.show()

# 10. Line chart showing trend (Date vs AQI)
df['Date'] = pd.to_datetime(df['Date'])
daily_aqi = df.groupby('Date')['AQI'].mean().reset_index()

plt.figure(figsize=(12, 4))
sns.lineplot(data=daily_aqi, x='Date', y='AQI', color='green')
plt.title("Daily Average AQI Over Time")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.tight_layout()
plt.show()


# 11. Correlation matrix and strongest pos/neg correlations
corr = df[numeric_cols.tolist() + ['AQI']].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.show()

# Strongest positive and negative correlation with AQI
corr_with_aqi = corr['AQI'].drop('AQI')
strong_pos = corr_with_aqi.idxmax()
strong_neg = corr_with_aqi.idxmin()
print(f"\nStrongest positive correlation with AQI: {strong_pos} ({corr_with_aqi[strong_pos]:.2f})")
print(f"Strongest negative correlation with AQI: {strong_neg} ({corr_with_aqi[strong_neg]:.2f})")


# 12. Scatter plots for both correlations
plt.figure(figsize=(6, 4))
sns.scatterplot(x=df[strong_pos], y=df['AQI'], color='blue')
plt.title(f"Scatter Plot: {strong_pos} vs AQI")
plt.xlabel(strong_pos)
plt.ylabel("AQI")
plt.tight_layout()
plt.show()

plt.figure(figsize=(6, 4))
sns.scatterplot(x=df[strong_neg], y=df['AQI'], color='red')
plt.title(f"Scatter Plot: {strong_neg} vs AQI")
plt.xlabel(strong_neg)
plt.ylabel("AQI")
plt.tight_layout()
plt.show()
