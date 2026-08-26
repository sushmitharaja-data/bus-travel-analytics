import streamlit as st
import pandas as pd
import os

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Prediction History",
    page_icon="🕐",
    layout="wide"
)

# ============================================================
# SIDEBAR + BUBBLE THEME
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

/* Bubble Cards */

.bubble-card {
    background: #171A21;
    border: 1px solid #2B303A;
    border-radius: 18px;
    padding: 22px;
    min-height: 125px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.18);
    transition: all 0.2s ease;
}

.bubble-card:hover {
    border-color: #20A9A3;
    transform: translateY(-2px);
}

.bubble-title {
    font-size: 15px;
    color: #A7ADB8;
    margin-bottom: 10px;
    font-weight: 500;
}

.bubble-value {
    font-size: 30px;
    font-weight: 700;
    color: #F5F7FA;
}

.section-bubble {
    background: #171A21;
    border: 1px solid #2B303A;
    border-radius: 18px;
    padding: 22px;
    margin-top: 10px;
    margin-bottom: 20px;
}

.stButton > button {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# PAGE HEADER
# ============================================================

st.title("🕐 Prediction History")

st.write(
    "View and analyse previously generated bus travel-time predictions."
)

st.divider()


# ============================================================
# HISTORY FILE
# ============================================================

history_file = "prediction_history.csv"


# ============================================================
# CHECK HISTORY
# ============================================================

if not os.path.exists(history_file):

    st.info("📭 No prediction history available yet.")

    st.write(
        "Go to **Trip Input → Analyze Trip → Prediction** "
        "to generate your first prediction."
    )

    st.stop()


# ============================================================
# LOAD HISTORY
# ============================================================

history_df = pd.read_csv(history_file)

if history_df.empty:

    st.info("📭 No prediction history available yet.")

    st.stop()


# ============================================================
# SUMMARY CALCULATIONS
# ============================================================

total_predictions = len(history_df)

average_prediction = history_df["Random Forest"].mean()

highest_prediction = history_df["Random Forest"].max()

lowest_prediction = history_df["Random Forest"].min()


# ============================================================
# HISTORY SUMMARY
# ============================================================

st.subheader("📊 History Summary")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.markdown(
        f"""
        <div class="bubble-card">
            <div class="bubble-title">
                🧾 Total Predictions
            </div>
            <div class="bubble-value">
                {total_predictions}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="bubble-card">
            <div class="bubble-title">
                ⏱️ Average Prediction
            </div>
            <div class="bubble-value">
                {average_prediction:.2f} min
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="bubble-card">
            <div class="bubble-title">
                🔴 Highest Prediction
            </div>
            <div class="bubble-value">
                {highest_prediction:.2f} min
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="bubble-card">
            <div class="bubble-title">
                🟢 Lowest Prediction
            </div>
            <div class="bubble-value">
                {lowest_prediction:.2f} min
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PREDICTION RECORDS
# ============================================================

st.divider()

st.subheader("🧾 Prediction Records")

st.markdown(
    '<div class="section-bubble">',
    unsafe_allow_html=True
)

st.dataframe(
    history_df,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PREDICTION TREND
# ============================================================

st.divider()

st.subheader("📈 Prediction Trend")

trend_df = pd.DataFrame({
    "Prediction": range(1, len(history_df) + 1),
    "Travel Time": history_df["Random Forest"]
})

trend_df = trend_df.set_index("Prediction")

st.markdown(
    '<div class="section-bubble">',
    unsafe_allow_html=True
)

st.line_chart(
    trend_df,
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MODEL COMPARISON
# ============================================================

st.divider()

st.subheader("🤖 Model Comparison")

model_df = history_df[
    [
        "Random Forest",
        "Linear Regression"
    ]
]

st.markdown(
    '<div class="section-bubble">',
    unsafe_allow_html=True
)

st.bar_chart(
    model_df,
    use_container_width=True
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# ROUTE HISTORY
# ============================================================

st.divider()

st.subheader("🛣️ Route Prediction History")

if "Route" in history_df.columns:

    route_summary = (
        history_df
        .groupby("Route")["Random Forest"]
        .mean()
        .reset_index()
    )

    route_summary = route_summary.rename(
        columns={
            "Random Forest":
            "Average Predicted Travel Time (min)"
        }
    )

    st.markdown(
        '<div class="section-bubble">',
        unsafe_allow_html=True
    )

    st.dataframe(
        route_summary,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# HISTORY MANAGEMENT
# ============================================================

st.divider()

st.subheader("🗑️ History Management")

st.write(
    "Clear all stored prediction records from the local history file."
)

if st.button(
    "🗑️ Clear All Prediction History",
    use_container_width=True
):

    os.remove(history_file)

    st.success(
        "✅ Prediction history cleared successfully."
    )

    st.rerun()


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🕐 Prediction history is stored locally in prediction_history.csv."
)
