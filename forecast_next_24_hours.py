
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load existing data
data = pd.read_csv("energy_dataset.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

# Create time-based features
data["hour"] = data["timestamp"].dt.hour
data["minute"] = data["timestamp"].dt.minute

X = data[["hour", "minute"]]
y = data["energy_consumption"]

# Train a simple demonstration model
model = LinearRegression()
model.fit(X, y)

# Create 24 future hourly timestamps
last_timestamp = data["timestamp"].max()

future_times = pd.date_range(
    start=last_timestamp + pd.Timedelta(hours=1),
    periods=24,
    freq="h"
)

future_data = pd.DataFrame({"timestamp": future_times})
future_data["hour"] = future_data["timestamp"].dt.hour
future_data["minute"] = future_data["timestamp"].dt.minute

# Predict future consumption
future_data["predicted_consumption"] = model.predict(
    future_data[["hour", "minute"]]
).clip(min=0)

# Save the forecast
future_data.to_csv("future_energy_forecast.csv", index=False)

print("CLEANTECH - NEXT 24 HOURS")
print(future_data.to_string(index=False))
print("\nForecast saved to future_energy_forecast.csv")
