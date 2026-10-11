
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load 30-day dataset
data = pd.read_csv("historical_energy_dataset.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])
data = data.sort_values("timestamp").reset_index(drop=True)

# Create time-based features
data["hour"] = data["timestamp"].dt.hour
data["minute"] = data["timestamp"].dt.minute
data["day_of_week"] = data["timestamp"].dt.dayofweek

# Use past and current simulated renewable generation
features = [
    "hour",
    "minute",
    "day_of_week",
    "solar_generation",
    "wind_generation"
]

X = data[features]
y = data["energy_consumption"]

# Keep the final 20% for testing, preserving time order
split_index = int(len(data) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]
y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42,
    min_samples_leaf=2
)

model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))

print("CLEANTECH - IMPROVED MODEL")
print("=" * 40)
print(f"Training records: {len(X_train)}")
print(f"Testing records: {len(X_test)}")
print(f"Mean Absolute Error (MAE): {mae:.2f} kWh")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f} kWh")

# Save evaluation predictions
results = pd.DataFrame({
    "timestamp": data["timestamp"].iloc[split_index:].values,
    "actual_consumption": y_test.values,
    "predicted_consumption": predictions
})

results.to_csv("improved_energy_predictions.csv", index=False)
print("\nSaved improved_energy_predictions.csv")
