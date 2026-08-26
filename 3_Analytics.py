import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Bus Analytics",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# SIDEBAR THEME
# ============================================================

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #073B3A 0%,
        #0B5250 45%,
        #0F6B68 100%
    );
}

[data-testid="stSidebar"] * {
    color: white !important;
}

[data-testid="stSidebarNav"] a {
    border-radius: 10px;
    margin: 5px 8px;
    padding: 10px 12px;
    transition: all 0.2s ease;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: #168F8A !important;
    transform: translateX(3px);
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #20A9A3 !important;
    font-weight: 700;
    box-shadow: 0 3px 10px rgba(0,0,0,0.25);
}

[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.25);
}


/* ============================================================
   MAIN HEADER
   ============================================================ */

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
}

.main-subtitle {
    font-size: 17px;
    color: #B8BEC9;
    margin-bottom: 25px;
}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.section-title {
    font-size: 25px;
    font-weight: 750;
    margin-top: 8px;
    margin-bottom: 18px;
}


/* ============================================================
   METRIC CARDS
   ============================================================ */

.metric-card {
    background: #181A21;
    border: 1px solid #2C303A;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    min-height: 120px;
}

.metric-label {
    font-size: 14px;
    color: #AEB4C0;
    margin-bottom: 8px;
}

.metric-value {
    font-size: 28px;
    font-weight: 800;
    color: #20C7C0;
}


/* ============================================================
   ANALYSIS CARDS
   ============================================================ */

.analysis-card {
    background: #181A21;
    border: 1px solid #2C303A;
    border-radius: 16px;
    padding: 20px 24px;
    min-height: 120px;
}

.analysis-label {
    font-size: 14px;
    color: #AEB4C0;
    margin-bottom: 8px;
}

.analysis-value {
    font-size: 24px;
    font-weight: 750;
    color: white;
    margin-bottom: 8px;
}


/* ============================================================
   DIVIDER
   ============================================================ */

.custom-divider {
    height: 1px;
    background: #30343E;
    margin: 30px 0;
}

</style>
""", unsafe_allow_html=True)


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
# PAGE HEADER
# ============================================================

st.markdown(
    '<div class="main-title">📊 Bus Travel Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Explore travel-time patterns, routes, directions and '
    'peak travel hours using historical bus data.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ANALYSIS FILTERS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🔎 Analysis Filters</div>',
    unsafe_allow_html=True
)


# IMPORTANT:
# No HTML filter-card is used here.
# This removes the unwanted empty bubble.

col1, col2, col3 = st.columns(3)


with col1:

    selected_direction = st.selectbox(
        "Direction",
        ["All"] + sorted(
            df["direction"].unique().tolist()
        )
    )


with col2:

    selected_start = st.selectbox(
        "Start Terminal",
        ["All"] + sorted(
            df["start_terminal"].unique().tolist()
        )
    )


with col3:

    selected_end = st.selectbox(
        "End Terminal",
        ["All"] + sorted(
            df["end_terminal"].unique().tolist()
        )
    )


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_direction != "All":

    filtered_df = filtered_df[
        filtered_df["direction"] == selected_direction
    ]


if selected_start != "All":

    filtered_df = filtered_df[
        filtered_df["start_terminal"] == selected_start
    ]


if selected_end != "All":

    filtered_df = filtered_df[
        filtered_df["end_terminal"] == selected_end
    ]


# ============================================================
# KEY STATISTICS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">📌 Key Statistics</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


# TOTAL TRIPS
with col1:

    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">🚌 Total Trips</div>'
        f'<div class="metric-value">{len(filtered_df):,}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# AVERAGE
with col2:

    if len(filtered_df) > 0:

        average_time = (
            filtered_df["duration_in_mins"].mean()
        )

        avg_value = f"{average_time:.2f} min"

    else:

        avg_value = "N/A"


    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">⏱️ Average Time</div>'
        f'<div class="metric-value">{avg_value}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# MAXIMUM
with col3:

    if len(filtered_df) > 0:

        maximum_time = (
            filtered_df["duration_in_mins"].max()
        )

        max_value = f"{maximum_time:.2f} min"

    else:

        max_value = "N/A"


    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">🔴 Maximum Time</div>'
        f'<div class="metric-value">{max_value}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# MINIMUM
with col4:

    if len(filtered_df) > 0:

        minimum_time = (
            filtered_df["duration_in_mins"].min()
        )

        min_value = f"{minimum_time:.2f} min"

    else:

        min_value = "N/A"


    st.markdown(
        f'<div class="metric-card">'
        f'<div class="metric-label">🟢 Minimum Time</div>'
        f'<div class="metric-value">{min_value}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ============================================================
# HOURLY ANALYSIS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">'
    '⏰ Average Travel Time by Hour'
    '</div>',
    unsafe_allow_html=True
)


hourly_avg = (
    filtered_df
    .groupby("hour")["duration_in_mins"]
    .mean()
)


if len(hourly_avg) > 0:

    # CHART
    st.line_chart(
        hourly_avg,
        use_container_width=True
    )


    # FIND PEAK AND FASTEST
    peak_hour = hourly_avg.idxmax()
    peak_time = hourly_avg.max()

    fastest_hour = hourly_avg.idxmin()
    fastest_time = hourly_avg.min()


    # ========================================================
    # PEAK / FASTEST CARDS
    # ========================================================

    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            f'<div class="analysis-card">'
            f'<div class="analysis-label">'
            f'🔴 Peak Travel Hour'
            f'</div>'
            f'<div class="analysis-value">'
            f'{peak_hour}:00'
            f'</div>'
            f'<div class="analysis-label">'
            f'Average: {peak_time:.2f} minutes'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )


    with col2:

        st.markdown(
            f'<div class="analysis-card">'
            f'<div class="analysis-label">'
            f'🟢 Fastest Travel Hour'
            f'</div>'
            f'<div class="analysis-value">'
            f'{fastest_hour}:00'
            f'</div>'
            f'<div class="analysis-label">'
            f'Average: {fastest_time:.2f} minutes'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )


else:

    st.info(
        "No data available for the selected filters."
    )


# ============================================================
# DIRECTION ANALYSIS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">'
    '🧭 Travel Time by Direction'
    '</div>',
    unsafe_allow_html=True
)


direction_avg = (
    filtered_df
    .groupby("direction")["duration_in_mins"]
    .mean()
)


if len(direction_avg) > 0:

    st.bar_chart(
        direction_avg,
        use_container_width=True
    )


    direction_table = (
        direction_avg
        .reset_index()
        .rename(
            columns={
                "duration_in_mins":
                "Average Travel Time (min)"
            }
        )
    )


    st.dataframe(
        direction_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No direction data available."
    )


# ============================================================
# ROUTE ANALYSIS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">'
    '🛣️ Route Performance'
    '</div>',
    unsafe_allow_html=True
)


route_avg = (
    filtered_df
    .groupby(
        [
            "start_terminal",
            "end_terminal"
        ]
    )["duration_in_mins"]
    .mean()
    .reset_index()
)


if len(route_avg) > 0:

    route_avg["Route"] = (
        route_avg["start_terminal"]
        + " → "
        + route_avg["end_terminal"]
    )


    route_table = route_avg[
        [
            "Route",
            "duration_in_mins"
        ]
    ].rename(
        columns={
            "duration_in_mins":
            "Average Travel Time (min)"
        }
    )


    st.dataframe(
        route_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No route data available."
    )


# ============================================================
# TOP 5 SLOWEST HOURS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">'
    '🐌 Top 5 Slowest Hours'
    '</div>',
    unsafe_allow_html=True
)


if len(hourly_avg) > 0:

    top_slow_hours = (
        hourly_avg
        .sort_values(ascending=False)
        .head(5)
    )


    slow_table = (
        top_slow_hours
        .reset_index()
    )


    slow_table.columns = [
        "Starting Hour",
        "Average Travel Time (min)"
    ]


    st.dataframe(
        slow_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No hourly data available."
    )


# ============================================================
# TOP 5 FASTEST HOURS
# ============================================================

st.markdown(
    '<div class="section-title">'
    '⚡ Top 5 Fastest Hours'
    '</div>',
    unsafe_allow_html=True
)


if len(hourly_avg) > 0:

    top_fast_hours = (
        hourly_avg
        .sort_values()
        .head(5)
    )


    fast_table = (
        top_fast_hours
        .reset_index()
    )


    fast_table.columns = [
        "Starting Hour",
        "Average Travel Time (min)"
    ]


    st.dataframe(
        fast_table,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info(
        "No hourly data available."
    )


# ============================================================
# FILTERED DATA PREVIEW
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">'
    '🔍 Filtered Data Preview'
    '</div>',
    unsafe_allow_html=True
)


st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.caption(
    "📊 Analytics are calculated from the historical "
    "bus trip dataset."
)
