# -*- coding: utf-8 -*-
"""titanic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1eZQqPt8cMbyBBusDifeOGtKFsn_kXH6B

# Titanic Data Analysis

**Exploratory Data Analysis (EDA) is a method of analyzing datasets to understand their main characteristics. It involves summarizing data features, detecting patterns, and uncovering relationships through visual and statistical techniques. **

## 1. Import Required Libraries
"""

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

"""##2. Load and Explore the Dataset




"""

# Load the Titanic dataset directly from seaborn
data = sns.load_dataset('titanic')

# Write code to display initial dataset information
print("Initial Dataset Info:\n")

# Write code to display the first few rows of the dataset
print("First Few Rows of the Dataset:\n")
print(data.head())


# Write code to display the last few rows of the dataset
print("\nLast Few Rows of the Dataset:\n")
print(data.tail())


# Write code to display the shape of the dataset (number of rows and columns)
print("\nShape of the Dataset:\n")
print(data.shape)

"""## 3.Check for Missing values"""

# Write code to calculate the count of missing values in each column
missing_values = data.isnull().sum()


# Write code to calculate the percentage of missing values in each column
missing_percentage = (missing_values / len(data)) * 100

# Display missing values count and percentage
print("\nMissing Values Count:\n", missing_values)
print("\nMissing Values Percentage:\n", missing_percentage)

"""## 4. Handle Missing Values"""

# Explanation: Replacing missing values ensures the dataset is complete and suitable for analysis.

# Write code for - 'Age': Replace missing values with the mean age
data['age'] = data['age'].fillna(data['age'].mean())

# Write code for - 'Embarked': Replace missing values with the mode (most frequent value)
data['embarked'] = data['embarked'].fillna(data['embarked'].mode()[0])

# Write code for - 'Fare': Replace missing values with zero
data['fare'] = data['fare'].fillna(0)

# Write code for - 'Deck': Add 'Unknown' as a new category and replace missing values with 'Unknown'
# Add 'Unknown' to the categories of the 'deck' column
data['deck'] = data['deck'].cat.add_categories('Unknown')
data['deck'] = data['deck'].fillna('Unknown')

# Write code for - 'Embark_town': Replace missing values with the mode (most frequent value)
data['embark_town'] = data['embark_town'].fillna(data['embark_town'].mode()[0])

# Write code for - Display missing values count
print("\nMissing Values Count After Handling:\n", data.isnull().sum())

# Calculate the percentage of missing values after handling
missing_values_after = data.isnull().sum()
missing_percentage_after = (missing_values_after / len(data)) * 100

# Write code for - Percentage after imputation
print("\nMissing Values Percentage After Handling:\n", missing_percentage_after)

"""##5. Remove Duplicates"""

# Write code for - Removing duplicates ensures that each entry in the dataset is unique.
print("Duplicated rows: ",data.duplicated().sum())

data.drop_duplicates(inplace=True)

print(f"\nDuplicates removed. Number of rows now: {len(data)}")

"""##6. Correct Data Types"""

# Explanation: Ensuring correct data types helps in proper analysis and computation.

# Write code for - converting 'age' and 'fare' to float
data['age'] = data['age'].astype(float)
data['fare'] = data['fare'].astype(float)

# Write code for - convert 'sex' and 'embarked' to categorical
data['sex'] = data['sex'].astype('category')
data['embarked'] = data['embarked'].astype('category')

data = data.copy()  # Create a copy to avoid SettingWithCopyWarning

"""##7. Normalize or Standardize the Data"""

# Explanation: Standardizing numerical features ensures they are on the same scale.

# Write code for - standardize the 'age' and 'fare' columns
scaler = StandardScaler()
data[['age', 'fare']] = scaler.fit_transform(data[['age', 'fare']])

"""##8. Create New Features (Feature Engineering)"""

# Explanation: Feature engineering can provide additional insights and improve model performance.

# Write code for - create a new feature 'family_size' which is the sum of 'sibsp' and 'parch' plus 1
data['family_size'] = data['sibsp'] + data['parch'] + 1

"""##9. Aggregation"""

# Explanation: Aggregation provides insights into how features vary across different classes.

# Write code for - group by 'pclass' and calculate the mean of 'age' and 'fare'
agg_data = data.groupby('pclass')[['age', 'fare']].mean()
print("\nAggregated Data by Pclass:\n", agg_data)

"""##10. Outlier Detection and Removal"""

# Explanation: Detecting and removing outliers helps improve the quality of the data.

# Plotting boxplot to detect outliers in 'fare'
plt.figure(figsize=(8,6))
sns.boxplot(x=data['fare'])
plt.title("Boxplot of 'Fare' to Detect Outliers")
plt.show()

plt.savefig('boxplot_fare.png', dpi=300)

# Removing outliers where 'Fare' is greater than 200
data = data[data['fare'] < 200]
print("\nOutliers removed based on Fare > 200.\n")

"""##11. Separate Numerical and Categorical Variables"""

# Explanation: Separating variables helps in organizing the data for more targeted analysis.

numerical_features = data.select_dtypes(include=['float64', 'int64'])
categorical_features = data.select_dtypes(include=['object', 'category', 'bool'])

print("\nNumerical Features:\n", numerical_features.head())
print("\nCategorical Features:\n", categorical_features.head())

"""##12. Data Visualization"""

# Explanation: Visualization helps to understand the distribution, relationships, and patterns in the data.

# Univariate Analysis: Age and Fare Distribution
plt.figure(figsize=(8,6))
sns.histplot(data['age'], kde=True, bins=20)
plt.title("Standardized Age Distribution")
plt.show()
plt.savefig("Standardized Age Distribution.png")

plt.figure(figsize=(8,6))
sns.histplot(data['fare'], kde=True, bins=20)
plt.title("Standardized Fare Distribution")
plt.show()
plt.savefig("Standardized Fare Distribution.png")

# Bivariate Analysis: Scatterplot of Age vs Fare
plt.figure(figsize=(8,6))
sns.scatterplot(x=data['age'], y=data['fare'])
plt.title("Age vs Fare")
plt.show()
plt.savefig("Scatter plot Age vs Fare.png")

# Heatmap to show correlation between numerical features
plt.figure(figsize=(10, 8))
sns.heatmap(data[['age', 'fare', 'sibsp', 'parch', 'family_size']].corr(), annot=True, cmap='coolwarm')
plt.title("Heatmap of Correlation Between Features")
plt.show()
plt.savefig("Heatmap of Correlation Between Features.png")


# Boxplot of 'Pclass' vs 'Fare'
plt.figure(figsize=(8,6))
sns.boxplot(x='pclass', y='fare', data=data)
plt.title('Boxplot of Pclass vs Fare')
plt.show()
plt.savefig("Boxplot of Pclass vs Fare.png")

"""##13. Descriptive Statistics"""

# Explanation: Descriptive statistics provide insights into the central tendency and dispersion of the features.

# Write code for - measuring of central tendency for 'age' and 'fare'
mean_age = data['age'].mean()
mean_fare = data['fare'].mean()
median_age = data['age'].median()
median_fare = data['fare'].median()
mode_age = data['age'].mode()[0]
mode_fare = data['fare'].mode()[0]

print(f"\nMean Age: {mean_age}, Median Age: {median_age}, Mode Age: {mode_age}")
print(f"Mean Fare: {mean_fare}, Median Fare: {median_fare}, Mode Fare: {mode_fare}")

# Write code that measures of dispersion for 'age' and 'fare'
range_age = data['age'].max() - data['age'].min()
range_fare = data['fare'].max() - data['fare'].min()
variance_age = data['age'].var()
variance_fare = data['fare'].var()
std_dev_age = data['age'].std()
std_dev_fare = data['fare'].std()

print(f"\nAge - Range: {range_age}, Variance: {variance_age}, Std Dev: {std_dev_age}")
print(f"Fare - Range: {range_fare}, Variance: {variance_fare}, Std Dev: {std_dev_fare}")

# Summary of the data (Descriptive Statistics)
print("\nSummary Statistics:\n", data.describe())

"""#Linear Regression"""

# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

"""##2: Check Column Names"""

# Check the column names in the dataset
print("Columns in the dataset:", data.columns)

"""##3: Drop Irrelevant Columns"""

# Drop irrelevant columns based on the dataset and correlation analysis
# Write code for dropping Columns such as 'survived', 'who', 'alive', and 'alone' are considered irrelevant for predicting 'fare'
data_cleaned = data.drop(columns=['survived', 'who', 'alive', 'alone'], errors='ignore')

# Check the updated columns after dropping irrelevant ones
print("Features in the dataset:", data_cleaned.columns)

"""##4: Define Features"""

# Define numerical and categorical features
# Numerical features include 'age', 'sibsp', 'parch', and 'family_size'
numerical_features = ['age', 'sibsp', 'parch', 'fare']
# Categorical features include 'sex', 'embarked', 'class', 'adult_male', 'deck', 'embark_town', and 'pclass'
categorical_features = [
    'sex', 'embarked', 'class', 'adult_male',
    'deck', 'embark_town', 'pclass']
# write your code here

"""##5: Prepare Features and Target Variable"""

# Separate features and target variable
# 'X' contains all the features (both numerical and categorical) except 'fare'
# 'y' is the target variable which is 'fare'

# write your code here

X = data[numerical_features + categorical_features].drop(columns='fare')
y = data['fare']

"""##6: Handle Categorical Variables and Standardize Numerical Features"""

# Handle categorical variables by one-hot encoding
# This will convert categorical features into numerical format using one-hot encoding
X = pd.get_dummies(X, columns=categorical_features)

# Standardize the numerical features
# StandardScaler will normalize numerical features to have a mean of 0 and a standard deviation of 1
scaler = StandardScaler()
numerical_features = ['age', 'sibsp', 'parch']
X[numerical_features] = scaler.fit_transform(X[numerical_features])

"""##7: Split Dataset"""

# Split the dataset into training and testing sets
# 80% of the data will be used for training, and 20% for testing

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

"""##8: Initialize and Train the Model"""

# Initialize the Linear Regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

"""##9: Predict and Evaluate"""

# Predict the fare on the test data
y_pred = model.predict(X_test)

# Evaluate the model performance
# Calculate Mean Squared Error, R-squared, and Mean Absolute Error
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
print(f"Mean Absolute Error: {mae}")

"""##10: Visualize Results"""

# Visualizing actual vs predicted fares
plt.figure(figsize=(8,6))
plt.scatter(y_test, y_pred, color="blue", label="Predicted")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2, label="Ideal Fit")
plt.xlabel('Actual Fare')
plt.ylabel('Predicted Fare')
plt.title('Actual vs Predicted Fare')
plt.legend()
plt.show()

plt.savefig('Actual vs Predicted Fare.png')