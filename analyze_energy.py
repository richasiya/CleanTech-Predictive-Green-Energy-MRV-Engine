
import pandas as pd

# Load the generated energy dataset
data = pd.read_csv("energy_dataset.csv")

# Display basic information
print("CLEAN TECH - ENERGY DATA ANALYSIS")
print("=" * 40)

print("\nDataset shape:")
print(data.shape)

print("\nFirst 5 records:")
print(data.head())

print("\nAverage energy metrics:")
print(
    data[
        [
            "solar_generation",
            "wind_generation",
            "energy_consumption",
            "renewable_generation",
            "energy_deficit",
            "renewable_matching_percent",
        ]
    ].mean().round(2)
)

# Find intervals with an energy deficit
deficit_data = data[data["energy_deficit"] > 0]

print("\nIntervals with energy deficit:", len(deficit_data))
print("\nFirst 5 deficit intervals:")
print(
    deficit_data[
        ["timestamp", "energy_consumption", "renewable_generation",
         "energy_deficit"]
    ].head()
)

# Save the analysis result
deficit_data.to_csv("energy_deficit_report.csv", index=False)

print("\nDeficit report saved successfully!")
