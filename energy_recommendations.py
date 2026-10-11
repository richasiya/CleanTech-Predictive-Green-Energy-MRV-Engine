
import pandas as pd

# Load energy data
data = pd.read_csv("energy_dataset.csv")

# Identify energy deficit and surplus
data["energy_surplus"] = (
    data["renewable_generation"] - data["energy_consumption"]
).clip(lower=0)

deficit_periods = data[data["energy_deficit"] > 0].copy()
surplus_periods = data[data["energy_surplus"] > 0].copy()

print("CLEANTECH - ENERGY-SAVING RECOMMENDATIONS")
print("=" * 50)

if not deficit_periods.empty:
    print("\nIntervals with an energy deficit:")
    for _, row in deficit_periods.head(5).iterrows():
        print(
            f"{row['timestamp']}: deficit of "
            f"{row['energy_deficit']:.2f} kWh"
        )
else:
    print("\nNo energy deficit intervals found.")

if not surplus_periods.empty:
    print("\nIntervals with renewable energy surplus:")
    for _, row in surplus_periods.head(5).iterrows():
        print(
            f"{row['timestamp']}: surplus of "
            f"{row['energy_surplus']:.2f} kWh"
        )
else:
    print("\nNo renewable energy surplus intervals found.")

# Create recommendations report
recommendations = []

for _, row in deficit_periods.iterrows():
    recommendations.append({
        "timestamp": row["timestamp"],
        "condition": "Energy Deficit",
        "energy_kwh": row["energy_deficit"],
        "recommendation": (
            "Consider shifting flexible loads to a surplus interval, "
            "if operationally feasible."
        )
    })

for _, row in surplus_periods.iterrows():
    recommendations.append({
        "timestamp": row["timestamp"],
        "condition": "Renewable Surplus",
        "energy_kwh": row["energy_surplus"],
        "recommendation": (
            "Consider scheduling flexible loads during this interval."
        )
    })

report = pd.DataFrame(recommendations)
report.to_csv("energy_recommendations.csv", index=False)

print("\nRecommendations saved to energy_recommendations.csv")
