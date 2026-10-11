
import pandas as pd
import matplotlib.pyplot as plt

# Load model predictions
data = pd.read_csv("improved_energy_predictions.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

# Plot actual and predicted consumption
plt.figure(figsize=(14, 6))

plt.plot(
    data["timestamp"],
    data["actual_consumption"],
    label="Actual Consumption"
)

plt.plot(
    data["timestamp"],
    data["predicted_consumption"],
    label="Predicted Consumption"
)

plt.title("CleanTech: Actual vs Predicted Energy Consumption")
plt.xlabel("Date")
plt.ylabel("Energy Consumption (kWh)")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save graph
plt.savefig("model_evaluation.png")
plt.show()

print("Model evaluation graph saved successfully!")
