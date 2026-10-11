
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the energy dataset
data = pd.read_csv("energy_dataset.csv")

# Create time-based features
data["timestamp"] = pd.to_datetime(data["timestamp"])
data["hour"] = data["timestamp"].dt.hour
data["minute"] = data["timestamp"].dt.minute

# Input features and target
X = data[["hour", "minute", "solar_generation", "wind_generation"]]
y = data["energy_consumption"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, predictions)

print("CLEANTECH - ENERGY CONSUMPTION MODEL")
print("-" * 40)
print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")
print(f"Mean Absolute Error (MAE): {mae:.2f} kWh")

# Save test predictions
results = pd.DataFrame({
    "Actual Consumption": y_test.values,
    "Predicted Consumption": predictions
})

results.to_csv("energy_predictions.csv", index=False)
print("\nPredictions saved to energy_predictions.csv")
