
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="CleanTech | Energy Intelligence",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).resolve().parent

# --------------------------------------------------
# ECO GREEN LIGHT THEME
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #F5F8F5;
    }

    [data-testid="stHeader"] {
        background: rgba(245, 248, 245, 0.95);
    }

    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E1EAE1;
    }

    [data-testid="stSidebar"] h1 {
        color: #166534;
        font-size: 24px;
    }

    .hero {
        background: linear-gradient(115deg, #14532D, #24834A);
        padding: 30px;
        border-radius: 18px;
        color: white;
        margin-bottom: 24px;
    }

    .hero h1 {
        color: white;
        font-size: 30px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #E5F5E9;
        font-size: 14px;
        margin-bottom: 0;
    }

    .section-title {
        color: #164E2A;
        font-size: 21px;
        font-weight: 700;
        margin-top: 18px;
        margin-bottom: 12px;
    }

    .metric-card {
        background: #FFFFFF;
        padding: 20px;
        border: 1px solid #E1EAE1;
        border-radius: 15px;
        min-height: 125px;
        box-shadow: 0 3px 12px rgba(22, 101, 52, 0.04);
    }

    .metric-label {
        color: #647568;
        font-size: 13px;
        font-weight: 500;
        margin-bottom: 12px;
    }

    .metric-value {
        color: #14532D;
        font-size: 26px;
        font-weight: 800;
        overflow-wrap: anywhere;
    }

    .metric-note {
        color: #718174;
        font-size: 11px;
        margin-top: 8px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF;
        border-color: #E1EAE1;
        border-radius: 15px;
    }

    .status-note {
        background: #EAF5EC;
        color: #245C35;
        padding: 13px 16px;
        border-radius: 10px;
        border-left: 4px solid #299653;
        font-size: 13px;
        margin: 10px 0 18px 0;
    }

    div.stButton > button,
    div.stDownloadButton > button {
        border-radius: 9px;
        border: 1px solid #B8D9C0;
    }

    h1, h2, h3 {
        color: #173D25;
    }

    [data-testid="stDataFrame"] {
        border: 1px solid #E1EAE1;
        border-radius: 10px;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------
def load_csv(filename):
    """Load a CSV file from the project directory."""
    path = BASE_DIR / filename

    if not path.exists():
        return None

    try:
        return pd.read_csv(path)
    except Exception as error:
        st.error(f"Could not read {filename}: {error}")
        return None




def metric_card(label, value, note):
    st.markdown(
        f"""
        <div style="background: linear-gradient(145deg, #FFFFFF, #F0F8F1);
                    padding: 22px;
                    border: 1px solid #DCEBDE;
                    border-radius: 16px;
                    min-height: 132px;
                    box-shadow: 0 5px 16px rgba(22, 101, 52, 0.06);">
            <div style="color: #5E7462; font-size: 12px;
                        font-weight: 700; margin-bottom: 15px;">
                {label}
            </div>
            <div style="color: #14532D; font-size: 28px;
                        font-weight: 800; line-height: 1.2;">
                {value}
            </div>
            <div style="color: #718174; font-size: 12px;
                        margin-top: 10px;">
                {note}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    



def section_title(title):
    st.markdown(
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# LOAD EXISTING PROJECT DATA
# --------------------------------------------------
data = load_csv("energy_dataset.csv")
forecast = load_csv("future_energy_forecast.csv")
predictions = load_csv("energy_predictions.csv")
improved = load_csv("improved_energy_predictions.csv")
recommendations = load_csv("energy_recommendations.csv")
deficit_report = load_csv("energy_deficit_report.csv")
metrics_summary = load_csv("energy_metrics_summary.csv")

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
with st.sidebar:
    st.markdown("# 🌱 CleanTech")
    st.caption("PREDICTIVE ENERGY INTELLIGENCE")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Energy Analytics",
            "Forecasting",
            "Recommendations",
            "Reports & Data"
        ],
        label_visibility="visible"
    )

    st.divider()

    st.markdown("**Project status**")
    st.caption("Academic prototype")
    st.caption("Data source: Simulated energy data")

    st.divider()
    st.caption("CleanTech MRV Engine · 2026")


# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>CleanTech Energy Intelligence</h1>
    <p>
        Monitor renewable energy, analyze consumption,
        evaluate predictions, and explore energy-saving opportunities.
    </p>
</div>
""", unsafe_allow_html=True)

if data is None:
    st.error(
        "energy_dataset.csv was not found. "
        "Keep it in the same folder as app.py."
    )
    st.stop()

required_columns = [
    "energy_consumption",
    "renewable_generation",
    "renewable_matched",
    "energy_deficit"
]

missing = [column for column in required_columns if column not in data.columns]

if missing:
    st.error(f"Required columns are missing from energy_dataset.csv: {missing}")
    st.stop()

for column in required_columns:
    data[column] = pd.to_numeric(data[column], errors="coerce")

data = data.dropna(subset=required_columns).copy()

if data.empty:
    st.error("The energy dataset contains no valid records.")
    st.stop()

total_consumption = data["energy_consumption"].sum()
total_renewable = data["renewable_generation"].sum()
total_matched = data["renewable_matched"].sum()
total_deficit = data["energy_deficit"].sum()

matching_percentage = (
    total_matched / total_consumption * 100
    if total_consumption > 0 else 0
)

st.markdown(
    '<div class="status-note">'
    '● Prototype running &nbsp; | &nbsp; '
    'Metrics calculated from the initial energy dataset'
    '</div>',
    unsafe_allow_html=True
)


# ==================================================
# PAGE 1: OVERVIEW
# ==================================================

if page == "Overview":
    # Page heading
    st.markdown(
        """
        <div style="margin-bottom: 22px;">
            <div style="color:#24834A; font-size:12px;
                        font-weight:700; letter-spacing:2px;">
                ENERGY INTELLIGENCE / OVERVIEW
            </div>
            <h2 style="margin:8px 0 4px 0; color:#164E2A;">
                Your Energy at a Glance
            </h2>
            <p style="color:#718174; margin:0;">
                Monitor renewable generation, consumption,
                and energy matching performance.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # KPI cards
    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:
        metric_card(
            "⚡ ENERGY CONSUMPTION",
            f"{total_consumption:,.1f}",
            "Total demand · kWh"
        )

    with c2:
        metric_card(
            "🌿 RENEWABLE GENERATION",
            f"{total_renewable:,.1f}",
            "Solar + wind · kWh"
        )

    with c3:
        metric_card(
            "↗ ENERGY DEFICIT",
            f"{total_deficit:,.1f}",
            "Unmatched demand · kWh"
        )

    with c4:
        metric_card(
            "♻ RENEWABLE MATCHING",
            f"{matching_percentage:.1f}%",
            "Matched energy / total demand"
        )

    st.write("")

    # Main chart section
    left, right = st.columns([1.65, 1], gap="medium")

    with left:
        with st.container(border=True):
            st.markdown("### Energy Performance")
            st.caption("Renewable supply compared with energy demand")

            if "timestamp" in data.columns:
                chart_data = data.copy()
                chart_data["timestamp"] = pd.to_datetime(
                    chart_data["timestamp"], errors="coerce"
                )
                chart_data = chart_data.dropna(subset=["timestamp"])
                chart_data = chart_data.sort_values("timestamp")
                chart_data = chart_data.set_index("timestamp")

                chart_data = chart_data[
                    ["renewable_generation", "energy_consumption"]
                ].resample("1h").mean()

                st.line_chart(
                    chart_data,
                    color=["#239653", "#E5A33D"],
                    height=320
                )
            else:
                st.info("Timestamp data is unavailable.")

    with right:
        with st.container(border=True):
            st.markdown("### Renewable Mix")
            st.caption("Generation by energy source")

            if (
                "solar_generation" in data.columns
                and "wind_generation" in data.columns
            ):
                source_data = pd.DataFrame({
                    "Source": ["Solar", "Wind"],
                    "Generation": [
                        data["solar_generation"].sum(),
                        data["wind_generation"].sum()
                    ]
                }).set_index("Source")

                st.bar_chart(
                    source_data,
                    color="#239653",
                    height=250
                )

                st.divider()

                st.metric(
                    "Renewable Energy Matched",
                    f"{total_matched:,.1f} kWh"
                )
            else:
                st.info("Solar and wind breakdown is unavailable.")

    # Recent data preview
    st.write("")
    with st.container(border=True):
        st.markdown("### Recent Energy Records")
        st.caption("A quick look at the latest available observations.")

        preview = data.tail(8).copy()

        if "timestamp" in preview.columns:
            preview["timestamp"] = pd.to_datetime(
                preview["timestamp"], errors="coerce"
            )

        st.dataframe(
            preview,
            use_container_width=True,
            hide_index=True
        )

        with st.expander("View complete dataset"):
            st.dataframe(
                data,
                use_container_width=True,
                hide_index=True
            )

    


# ==================================================
# PAGE 2: ENERGY ANALYTICS
# ==================================================
elif page == "Energy Analytics":
    section_title("Energy Analytics")
    st.caption("Explore energy demand, renewable generation, and deficits.")

    c1, c2, c3 = st.columns(3)

    c1.metric("Total Renewable Generation", f"{total_renewable:,.2f} kWh")
    c2.metric("Total Matched Energy", f"{total_matched:,.2f} kWh")
    c3.metric("Total Energy Deficit", f"{total_deficit:,.2f} kWh")

    if "timestamp" in data.columns:
        analytic_data = data.copy()
        analytic_data["timestamp"] = pd.to_datetime(
            analytic_data["timestamp"], errors="coerce"
        )
        analytic_data = analytic_data.dropna(subset=["timestamp"])

        with st.container(border=True):
            st.markdown("**Generation and Consumption Trends**")
            st.line_chart(
                analytic_data.set_index("timestamp")[
                    ["solar_generation", "wind_generation",
                     "energy_consumption"]
                ] if all(
                    col in analytic_data.columns
                    for col in [
                        "solar_generation",
                        "wind_generation",
                        "energy_consumption"
                    ]
                ) else analytic_data.set_index("timestamp")[
                    ["renewable_generation", "energy_consumption"]
                ],
                height=350
            )

    if "renewable_matching_percent" in data.columns:
        with st.container(border=True):
            st.markdown("**Renewable Matching Percentage by Interval**")
            matching_data = data.copy()

            if "timestamp" in matching_data.columns:
                matching_data["timestamp"] = pd.to_datetime(
                    matching_data["timestamp"], errors="coerce"
                )
                matching_data = matching_data.dropna(subset=["timestamp"])
                matching_data = matching_data.set_index("timestamp")

            st.line_chart(
                matching_data["renewable_matching_percent"],
                color="#239653",
                height=250
            )

    with st.expander("View intervals with an energy deficit"):
        deficit_data = data[data["energy_deficit"] > 0]
        st.write(f"Intervals with deficit: {len(deficit_data)}")
        st.dataframe(deficit_data, use_container_width=True, hide_index=True)

    with st.expander("View the complete dataset"):
        st.dataframe(data, use_container_width=True, hide_index=True)


# ==================================================
# PAGE 3: FORECASTING
# ==================================================
elif page == "Forecasting":
    section_title("Energy Forecasting")
    st.caption("Review the preliminary forecast and model evaluation results.")

    if forecast is not None and not forecast.empty:
        forecast["timestamp"] = pd.to_datetime(
            forecast["timestamp"], errors="coerce"
        )

        if "predicted_consumption" in forecast.columns:
            with st.container(border=True):
                st.markdown("**Preliminary Next 24-Hour Consumption Forecast**")
                st.line_chart(
                    forecast.dropna(subset=["timestamp"]).set_index("timestamp")[
                        ["predicted_consumption"]
                    ],
                    color="#239653",
                    height=300
                )

            with st.expander("View forecast records"):
                st.dataframe(forecast, use_container_width=True, hide_index=True)

            st.download_button(
                "Download Future Forecast",
                forecast.to_csv(index=False),
                file_name="future_energy_forecast.csv",
                mime="text/csv"
            )
    else:
        st.info(
            "Forecast file not found. Run forecast_next_24_hours.py "
            "to generate it."
        )

    if improved is not None and not improved.empty:
        needed = {"actual_consumption", "predicted_consumption"}

        if needed.issubset(improved.columns):
            with st.container(border=True):
                st.markdown("**Random Forest: Actual vs Predicted**")

                plot_data = improved[
                    ["actual_consumption", "predicted_consumption"]
                ].copy()

                plot_data.columns = ["Actual", "Predicted"]

                st.line_chart(
                    plot_data,
                    color=["#239653", "#E5A33D"],
                    height=300
                )

            with st.expander("View model evaluation records"):
                st.dataframe(improved, use_container_width=True, hide_index=True)

            st.download_button(
                "Download Model Results",
                improved.to_csv(index=False),
                file_name="improved_energy_predictions.csv",
                mime="text/csv"
            )

    if predictions is not None and not predictions.empty:
        with st.expander("View initial Linear Regression predictions"):
            st.dataframe(predictions, use_container_width=True, hide_index=True)


# ==================================================
# PAGE 4: RECOMMENDATIONS
# ==================================================
elif page == "Recommendations":
    section_title("Energy-Saving Recommendations")
    st.caption("Identify surplus periods and intervals with unmatched demand.")

    if recommendations is not None and not recommendations.empty:
        if "condition" in recommendations.columns:
            deficit_count = (
                recommendations["condition"] == "Energy Deficit"
            ).sum()

            surplus_count = (
                recommendations["condition"] == "Renewable Surplus"
            ).sum()

            c1, c2 = st.columns(2)
            c1.metric("Deficit Intervals", int(deficit_count))
            c2.metric("Surplus Intervals", int(surplus_count))

        st.dataframe(
            recommendations,
            use_container_width=True,
            hide_index=True
        )

        st.download_button(
            "Download Recommendations",
            recommendations.to_csv(index=False),
            file_name="energy_recommendations.csv",
            mime="text/csv"
        )
    else:
        st.info(
            "Recommendations file not found. Run "
            "energy_recommendations.py first."
        )

    if deficit_report is not None:
        with st.expander("View detailed energy deficit report"):
            st.dataframe(
                deficit_report,
                use_container_width=True,
                hide_index=True
            )

    st.caption(
        "Recommendations are rule-based suggestions using simulated data. "
        "Operational feasibility and safety must be checked before shifting loads."
    )


# ==================================================
# PAGE 5: REPORTS AND DATA
# ==================================================
elif page == "Reports & Data":
    section_title("Reports & Data")
    st.caption("Inspect and download the files generated by your project.")

    report_options = {
        "Initial Energy Dataset": ("energy_dataset.csv", data),
        "Energy Deficit Report": ("energy_deficit_report.csv", deficit_report),
        "Energy Metrics Summary": ("energy_metrics_summary.csv", metrics_summary),
        "Initial Predictions": ("energy_predictions.csv", predictions),
        "Improved Model Results": (
            "improved_energy_predictions.csv", improved
        ),
        "Future Forecast": ("future_energy_forecast.csv", forecast),
        "Energy Recommendations": (
            "energy_recommendations.csv", recommendations
        )
    }

    for label, (filename, frame) in report_options.items():
        with st.container(border=True):
            left, right = st.columns([3, 1])

            with left:
                st.markdown(f"**{label}**")
                if frame is None:
                    st.caption("File not available yet.")
                else:
                    st.caption(f"{len(frame)} records")

            with right:
                if frame is not None:
                    st.download_button(
                        "Download",
                        frame.to_csv(index=False),
                        file_name=filename,
                        mime="text/csv",
                        key=f"download_{filename}"
                    )

            if frame is not None:
                with st.expander(f"Preview {filename}"):
                    st.dataframe(
                        frame,
                        use_container_width=True,
                        hide_index=True
                    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()
st.caption(
    "CleanTech Predictive Green Energy MRV Engine · "
    "Academic prototype using simulated data"
)
