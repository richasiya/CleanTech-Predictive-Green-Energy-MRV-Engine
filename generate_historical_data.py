
import numpy as np
import pandas as pd

np.random.seed(42)

# Generate 30 days of 15-minute interval data
timestamps = pd.date_range(
    start="2026-01-01",
    periods=30 * 24 * 4,
    freq="15min"
)

hour = timestamps.hour.to_numpy()
day = timestamps.dayofyear.to_numpy()

# Simulated solar generation: zero at night, higher during daytime
daylight = np.maximum(
    np.sin(np.pi * (hour - 6) / 12),
    0
)
solar = daylight * 80 + np.random.normal(0, 3, len(hour))
solar = np.clip(solar, 0, None)

# Simulated wind generation
wind = np.clip(
    25 + 10 * np.sin(2 * np.pi * day / 7)
    + np.random.normal(0, 5, len(hour)),
    0, None
)

# Simulated energy consumption: higher during daytime
consumption = np.clip(
    65 + 15 * np.sin(np.pi * (hour - 6) / 12)
    + 8 * np.sin(2 * np.pi * hour / 24)
    + np.random.normal(0, 5, len(hour)),
    20, None
)

data = pd.DataFrame({
    "timestamp": timestamps,
    "solar_generation": solar,
    "wind_generation": wind,
    "energy_consumption": consumption
})

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
    data["renewable_matched"] / data["energy_consumption"] * 100,
    0
)

data.to_csv("historical_energy_dataset.csv", index=False)

print("30-day simulated dataset generated successfully!")
print("Total records:", len(data))
print(data.head())
print("\nSaved as historical_energy_dataset.csv")
