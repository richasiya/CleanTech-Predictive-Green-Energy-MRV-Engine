
import pandas as pd

# Load the dataset
data = pd.read_csv("energy_dataset.csv")

# Calculate total energy values
total_consumption = data["energy_consumption"].sum()
total_renewable = data["renewable_generation"].sum()
total_matched = data["renewable_matched"].sum()
total_deficit = data["energy_deficit"].sum()

# Calculate renewable matching percentage
if total_consumption > 0:
    matching_percentage = (total_matched / total_consumption) * 100
else:
    matching_percentage = 0

# Display the results
print("CLEANTECH - ENERGY METRICS")
print("-" * 35)
print(f"Total Energy Consumption: {total_consumption:.2f} kWh")
print(f"Total Renewable Generation: {total_renewable:.2f} kWh")
print(f"Total Renewable Energy Matched: {total_matched:.2f} kWh")
print(f"Total Energy Deficit: {total_deficit:.2f} kWh")
print(f"Renewable Matching Percentage: {matching_percentage:.2f}%")

# Save the summary
summary = pd.DataFrame({
    "Metric": [
        "Total Energy Consumption",
        "Total Renewable Generation",
        "Total Renewable Energy Matched",
        "Total Energy Deficit",
        "Renewable Matching Percentage"
    ],
    "Value": [
        total_consumption,
        total_renewable,
        total_matched,
        total_deficit,
        matching_percentage
    ]
})

summary.to_csv("energy_metrics_summary.csv", index=False)
print("\nMetrics saved to energy_metrics_summary.csv")
