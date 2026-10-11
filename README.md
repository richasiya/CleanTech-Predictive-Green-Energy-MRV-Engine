# CleanTech: Predictive Green Energy MRV Engine

## Project Overview

An AI/ML-based academic project for renewable energy forecasting, energy deficit analysis, and data-driven recommendations. Currently in the prototype stage, using simulated energy data to demonstrate predictive analytics and green energy monitoring concepts.


## Features

- Renewable energy generation and consumption analysis
- Energy deficit and renewable matching calculations
- Interactive Streamlit dashboard
- Energy consumption prediction using Linear Regression and Random Forest
- Actual vs. predicted model evaluation
- Preliminary 24-hour consumption forecast
- Rule-based energy-saving recommendations
- Downloadable CSV reports and visualizations

## Technology Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Visualization:** Matplotlib, Streamlit
- **Data Storage:** CSV files

## Project Structure

- `app.py` — Interactive dashboard
- `generate_dataset.py` — Initial dataset generation
- `analyze_energy.py` — Energy deficit analysis
- `energy_metrics.py` — Energy metric calculations
- `energy_graph.py` — Renewable generation comparison
- `train_model.py` — Initial Linear Regression model
- `energy_recommendations.py` — Rule-based recommendations
- `forecast_next_24_hours.py` — Preliminary future forecast demonstration
- `generate_historical_data.py` — Generates 30 days of simulated data
- `improved_forecast_model.py` — Random Forest model training and evaluation
- `evaluate_model.py` — Model evaluation visualization

## Installation and Setup

1. Install Python.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Create and activate a virtual environment.
5. Install the required packages:

   `python -m pip install pandas numpy matplotlib scikit-learn streamlit`

6. Generate the initial dataset:

   `python generate_dataset.py`

7. Generate the historical dataset:

   `python generate_historical_data.py`

8. Train the improved model:

   `python improved_forecast_model.py`

9. Generate recommendations:

   `python energy_recommendations.py`

10. Start the dashboard:

    `python -m streamlit run app.py`

## Dataset

This prototype uses simulated energy generation and consumption data at 15-minute intervals. The historical dataset contains 30 days of simulated observations.

The results are intended for educational and experimental purposes, not real-world industrial energy control.

## Limitations and Future Scope

- Validate models on real energy datasets.
- Improve future forecasting using historical patterns and weather inputs.
- Forecast solar and wind generation independently.
- Add a database and API for storing and serving energy data.
- Develop more advanced load-shifting recommendations.
- Explore automated reporting and verification workflows.

## Project Status

Academic prototype under development.
