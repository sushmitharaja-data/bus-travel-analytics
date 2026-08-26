import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Insights",
    page_icon="🧠",
    layout="wide"
)

# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("bus_trips_654.csv")

df["start_time"] = pd.to_datetime(
    df["start_time"],
    format="%H:%M:%S"
)

df["hour"] = df["start_time"].dt.hour

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
"""
<style>

.insights-header {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.insights-subtitle {
    font-size: 17px;
    color: #B8BEC9;
    margin-bottom: 25px;
}

.section-title {
    font-size: 26px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 18px;
}

.divider {
    height: 1px;
    background: #30343E;
    margin: 30px 0;
}

/* =========================
   KPI CARDS
   ========================= */

.kpi-card {
    background: #181A21;
    border: 1px solid #2C303A;
    border-radius: 16px;
    padding: 22px;
    min-height: 135px;
    text-align: center;
}

.kpi-label {
    color: #AEB4C0;
    font-size: 15px;
    margin-bottom: 12px;
}

.kpi-value {
    color: #20C7C0;
    font-size: 27px;
    font-weight: 800;
}

/* =========================
   INSIGHT CARDS
   ========================= */

.insight-card {
    background: #181A21;
    border: 1px solid #2C303A;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 15px;
}

.insight-title {
    font-size: 20px;
    font-weight: 750;
    margin-bottom: 15px;
}

.insight-text {
    font-size: 16px;
    line-height: 1.7;
    color: #E5E7EB;
}

/* =========================
   RECOMMENDATION
   ========================= */

.recommendation-card {
    background: linear-gradient(
        135deg,
        #123F3D,
        #164B48
    );
    border: 1px solid #20A9A3;
    border-radius: 18px;
    padding: 28px;
    margin-top: 10px;
    box-shadow: 0 0 25px rgba(32,169,163,0.12);
}

.recommendation-title {
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 15px;
    color: white !important;
}

.recommendation-text {
    font-size: 17px;
    line-height: 1.8;
    color: white !important;
}

.recommendation-text b {
    color: white !important;
    font-weight: 800;
}

/* =========================
   SUMMARY CARD
   ========================= */

.summary-card {
    background: #181A21;
    border: 1px solid #2C303A;
    border-radius: 18px;
    padding: 20px;
}

</style>
""",
unsafe_allow_html=True
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="insights-header">🧠 Smart Bus Travel Insights</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="insights-subtitle">'
    'Automatically generated insights based on historical bus travel data.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

# ============================================================
# BASIC CALCULATIONS
# ============================================================

overall_average = df["duration_in_mins"].mean()

hourly_avg = (
    df.groupby("hour")["duration_in_mins"]
    .mean()
)

slowest_hour = hourly_avg.idxmax()
slowest_hour_time = hourly_avg.max()

fastest_hour = hourly_avg.idxmin()
fastest_hour_time = hourly_avg.min()

# ============================================================
# ROUTE ANALYSIS
# ============================================================

route_avg = (
    df.groupby(
        ["start_terminal", "end_terminal"]
    )["duration_in_mins"]
    .mean()
    .reset_index()
)

route_avg["Route"] = (
    route_avg["start_terminal"]
    + " → "
    + route_avg["end_terminal"]
)

slowest_route = route_avg.loc[
    route_avg["duration_in_mins"].idxmax()
]

fastest_route = route_avg.loc[
    route_avg["duration_in_mins"].idxmin()
]

# ============================================================
# DIRECTION ANALYSIS
# ============================================================

direction_avg = (
    df.groupby("direction")["duration_in_mins"]
    .mean()
)

highest_direction = direction_avg.idxmax()
highest_direction_time = direction_avg.max()

lowest_direction = direction_avg.idxmin()
lowest_direction_time = direction_avg.min()

direction_difference = (
    highest_direction_time -
    lowest_direction_time
)

# ============================================================
# KEY FINDINGS
# ============================================================

st.markdown(
    '<div class="section-title">📌 Key Findings</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">🔴 Peak Hour</div>'
        f'<div class="kpi-value">{slowest_hour}:00</div>'
        f'</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">🟢 Fastest Hour</div>'
        f'<div class="kpi-value">{fastest_hour}:00</div>'
        f'</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">🐌 Slowest Route</div>'
        f'<div class="kpi-value">{slowest_route["Route"]}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f'<div class="kpi-card">'
        f'<div class="kpi-label">⚡ Fastest Route</div>'
        f'<div class="kpi-value">{fastest_route["Route"]}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

# ============================================================
# PEAK HOUR INSIGHT
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">⏰ Peak Hour Insight</div>',
    unsafe_allow_html=True
)

difference = slowest_hour_time - overall_average

st.markdown(
    f'<div class="insight-card">'
    f'<div class="insight-title">🔴 Peak Travel Period</div>'
    f'<div class="insight-text">'
    f'The highest average travel time occurs around '
    f'<b>{slowest_hour}:00</b>.<br><br>'
    f'Average travel time during this period is '
    f'<b>{slowest_hour_time:.2f} minutes</b>.<br><br>'
    f'Overall average travel time is '
    f'<b>{overall_average:.2f} minutes</b>.<br><br>'
    f'During the peak hour, travel time is approximately '
    f'<b>{difference:.2f} minutes higher</b> than the overall average.'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True
)

# ============================================================
# BEST TRAVEL TIME
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🟢 Best Travel Time</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="insight-card">'
    f'<div class="insight-title">🟢 Recommended Travel Period</div>'
    f'<div class="insight-text">'
    f'The fastest average travel time occurs around '
    f'<b>{fastest_hour}:00</b>.<br><br>'
    f'Average travel time during this period is '
    f'<b>{fastest_hour_time:.2f} minutes</b>.<br><br>'
    f'Travelling around this time may result in a shorter '
    f'journey compared with the peak period.'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True
)

# ============================================================
# ROUTE PERFORMANCE
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🛣️ Route Performance</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-title">🐌 Slowest Route</div>'
        f'<div class="insight-text">'
        f'<b>{slowest_route["Route"]}</b><br><br>'
        f'Average Travel Time:<br>'
        f'<b>{slowest_route["duration_in_mins"]:.2f} minutes</b>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f'<div class="insight-card">'
        f'<div class="insight-title">⚡ Fastest Route</div>'
        f'<div class="insight-text">'
        f'<b>{fastest_route["Route"]}</b><br><br>'
        f'Average Travel Time:<br>'
        f'<b>{fastest_route["duration_in_mins"]:.2f} minutes</b>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True
    )

# ============================================================
# DIRECTION ANALYSIS
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🧭 Direction Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="insight-card">'
    f'<div class="insight-title">🧭 Direction Comparison</div>'
    f'<div class="insight-text">'
    f'Direction <b>{highest_direction}</b> has the higher '
    f'average travel time.<br><br>'
    f'Average: <b>{highest_direction_time:.2f} minutes</b><br><br>'
    f'It is approximately '
    f'<b>{direction_difference:.2f} minutes</b> slower than '
    f'Direction {lowest_direction}.'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True
)

# ============================================================
# SMART RECOMMENDATION
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">💡 Smart Recommendation</div>',
    unsafe_allow_html=True
)

if slowest_hour_time > overall_average * 1.10:

    recommendation = (
        f'Avoid travelling around <b>{slowest_hour}:00</b> '
        f'when possible, as this period has significantly '
        f'higher travel time.'
    )

else:

    recommendation = (
        'Travel times are relatively stable across the '
        'observed hours.'
    )

st.markdown(
    f'<div class="recommendation-card">'
    f'<div class="recommendation-title">'
    f'🚌 Travel Recommendation'
    f'</div>'
    f'<div class="recommendation-text">'
    f'{recommendation}'
    f'<br><br>'
    f'💡 For shorter travel time, consider travelling around '
    f'<b>{fastest_hour}:00</b>, based on historical data.'
    f'</div>'
    f'</div>',
    unsafe_allow_html=True
)

# ============================================================
# OVERALL SUMMARY
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">📋 Overall Summary</div>',
    unsafe_allow_html=True
)

summary_data = pd.DataFrame({
    "Insight": [
        "Overall Average Travel Time",
        "Peak Hour",
        "Peak Hour Average",
        "Fastest Hour",
        "Fastest Hour Average",
        "Slowest Route",
        "Fastest Route"
    ],
    "Value": [
        f"{overall_average:.2f} minutes",
        f"{slowest_hour}:00",
        f"{slowest_hour_time:.2f} minutes",
        f"{fastest_hour}:00",
        f"{fastest_hour_time:.2f} minutes",
        slowest_route["Route"],
        fastest_route["Route"]
    ]
})

st.markdown(
    '<div class="summary-card">',
    unsafe_allow_html=True
)

st.dataframe(
    summary_data,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

st.caption(
    "🧠 Insights are automatically generated from historical "
    "bus trip data."
)
