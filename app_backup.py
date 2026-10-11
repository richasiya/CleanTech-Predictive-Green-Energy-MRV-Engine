
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="CleanTech Energy Dashboard",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 CleanTech: Predictive Green Energy MRV Engine")
st.write("Monitor renewable energy generation, consumption, and energy deficits.")

# Load dataset
try:
    data = pd.read_csv("energy_dataset.csv")
except FileNotFoundError:
    st.error("energy_dataset.csv not found. Please check your project folder.")
    st.stop()

# Calculate metrics
total_consumption = data["energy_consumption"].sum()
total_renewable = data["renewable_generation"].sum()
total_matched = data["renewable_matched"].sum()
total_deficit = data["energy_deficit"].sum()

matching_percentage = (
    total_matched / total_consumption * 100
    if total_consumption > 0 else 0
)

# Display metric cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Consumption", f"{total_consumption:.2f} kWh")
col2.metric("Renewable Generation", f"{total_renewable:.2f} kWh")
col3.metric("Energy Deficit", f"{total_deficit:.2f} kWh")
col4.metric("Renewable Matching", f"{matching_percentage:.2f}%")

st.divider()

# Display dataset
st.subheader("Energy Data")
st.dataframe(data, use_container_width=True)

# Create comparison chart
st.subheader("Renewable Energy vs Consumption")

chart_data = data.set_index("timestamp")[
    ["renewable_generation", "energy_consumption"]
]

st.line_chart(chart_data)


# Display Machine Learning predictions
st.divider()
st.subheader("🤖 Energy Consumption: Actual vs Predicted")

try:
    predictions = pd.read_csv("energy_predictions.csv")

    st.line_chart(
        predictions.rename(columns={
            "Actual Consumption": "Actual",
            "Predicted Consumption": "Predicted"
        })
    )

    st.dataframe(predictions, use_container_width=True)

    st.download_button(
        "Download Energy Predictions",
        predictions.to_csv(index=False),
        file_name="energy_predictions.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.warning("Run train_model.py to generate energy predictions.")

# Show intervals with energy deficit
st.subheader("Energy Deficit Report")

deficit_data = data[data["energy_deficit"] > 0]

st.write(f"Intervals with an energy deficit: {len(deficit_data)}")
st.dataframe(deficit_data, use_container_width=True)

# Download reports
st.download_button(
    "Download Energy Dataset",
    data.to_csv(index=False),
    file_name="energy_dataset.csv",
    mime="text/csv"
)

st.download_button(
    "Download Energy Deficit Report",
    deficit_data.to_csv(index=False),
    file_name="energy_deficit_report.csv",
    mime="text/csv"
)


# Energy-saving recommendations
st.divider()
st.subheader("🌱 Energy-Saving Recommendations")

try:
    recommendations = pd.read_csv("energy_recommendations.csv")

    if recommendations.empty:
        st.info("No recommendations are available yet.")
    else:
        st.dataframe(recommendations, use_container_width=True)

        st.download_button(
            "Download Energy Recommendations",
            recommendations.to_csv(index=False),
            file_name="energy_recommendations.csv",
            mime="text/csv"
        )

except FileNotFoundError:
    st.warning(
        "Please run energy_recommendations.py to generate the report."
    )



# Future Energy Forecast
st.divider()
st.subheader("🔮 Next 24 Hours: Energy Consumption Forecast")

try:
    forecast = pd.read_csv("future_energy_forecast.csv")
    forecast["timestamp"] = pd.to_datetime(forecast["timestamp"])

    st.line_chart(
        forecast.set_index("timestamp")["predicted_consumption"]
    )

    st.dataframe(forecast, use_container_width=True)

    st.download_button(
        "Download 24-Hour Forecast",
        forecast.to_csv(index=False),
        file_name="future_energy_forecast.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.warning(
        "Run forecast_next_24_hours.py to generate the forecast."
    )


# Improved Model Evaluation
st.divider()
st.subheader("📊 Improved Model: Actual vs Predicted")

try:
    evaluation = pd.read_csv("improved_energy_predictions.csv")
    evaluation["timestamp"] = pd.to_datetime(evaluation["timestamp"])

    st.line_chart(
        evaluation.set_index("timestamp")[
            ["actual_consumption", "predicted_consumption"]
        ]
    )

    st.caption(
        "Evaluation on the final 20% of the simulated dataset, "
        "kept separate from the training period."
    )

    st.dataframe(evaluation, use_container_width=True)

    st.download_button(
        "Download Improved Model Results",
        evaluation.to_csv(index=False),
        file_name="improved_energy_predictions.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.warning(
        "Run improved_forecast_model.py to generate model results."
    )
