import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

print(df.head())


# Visualize correlations
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Matrix")
plt.show()


# Features and target
X = df[['reading score', 'writing score']]
y = df['math score']


# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train model
model = LinearRegression()
model.fit(X_train, y_train)


# Predictions
predictions = model.predict(X_test)


# Evaluate model
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# Plot results
plt.scatter(y_test, predictions)

plt.xlabel("Actual Math Scores")
plt.ylabel("Predicted Math Scores")

plt.title("Actual vs Predicted Scores")

plt.show()