
import pandas as pd
import matplotlib.pyplot as plt

# Load the energy dataset
data = pd.read_csv("energy_dataset.csv")

# Create the graph
plt.figure(figsize=(12, 6))

plt.plot(
    data["timestamp"],
    data["renewable_generation"],
    label="Renewable Energy Generation",
    marker="o"
)

plt.plot(
    data["timestamp"],
    data["energy_consumption"],
    label="Energy Consumption",
    marker="o"
)

plt.title("CleanTech: Renewable Energy vs Consumption")
plt.xlabel("Time")
plt.ylabel("Energy (kWh)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save and display the graph
plt.savefig("energy_comparison.png")
plt.show()

print("Graph saved successfully!")
