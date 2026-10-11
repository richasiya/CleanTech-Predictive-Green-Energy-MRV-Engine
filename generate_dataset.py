
import pandas as pd
import numpy as np

# Create one day of energy readings at 15-minute intervals
timestamps = pd.date_range(
    start="2026-01-01",
    periods=96,
    freq="15min"
)

np.random.seed(42)

data = pd.DataFrame({
    "timestamp": timestamps,
    "solar_generation": np.random.uniform(0, 50, 96).round(2),
    "wind_generation": np.random.uniform(5, 25, 96).round(2),
    "energy_consumption": np.random.uniform(30, 70, 96).round(2)
})

# Calculate renewable energy metrics
data["renewable_generation"] = (
    data["solar_generation"] + data["wind_generation"]
)

data["renewable_matched"] = np.minimum(
    data["renewable_generation"],
    data["energy_consumption"]
)

data["energy_deficit"] = np.maximum(
    data["energy_consumption"] - data["renewable_generation"],
    0
)

data["renewable_matching_percent"] = np.where(
    data["energy_consumption"] > 0,
    data["renewable_matched"]
    / data["energy_consumption"] * 100,
    0
).round(2)

# Save the dataset
data.to_csv("energy_dataset.csv", index=False)

print("CleanTech dataset created successfully!")
print(data.head(10))
print("\nTotal records:", len(data))
