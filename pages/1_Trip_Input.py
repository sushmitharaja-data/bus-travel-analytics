
import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Trip Input | TransitIQ",
    page_icon="📍",
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
    margin: 4px 8px;
    padding: 10px 12px;
}

[data-testid="stSidebarNav"] a:hover {
    background-color: #168F8A !important;
}

[data-testid="stSidebarNav"] a[aria-current="page"] {
    background-color: #20A9A3 !important;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# PAGE HEADER
# ============================================================

st.title("📍 Trip Input")

st.write(
    "Enter the trip details to estimate the bus travel time."
)

st.divider()

# ============================================================
# TRIP INFORMATION
# ============================================================

st.subheader("🚌 Trip Information")

col1, col2 = st.columns(2)

# ============================================================
# LEFT COLUMN
# ============================================================

with col1:

    hour = st.number_input(
        "🕐 Starting Hour",
        min_value=0,
        max_value=23,
        value=8,
        step=1
    )

    direction = st.selectbox(
        "🧭 Direction",
        [1, 2]
    )

# ============================================================
# RIGHT COLUMN
# ============================================================

with col2:

    start_terminal = st.selectbox(
        "📍 Start Terminal",
        ["BT01", "BT02"]
    )

    end_terminal = st.selectbox(
        "🏁 End Terminal",
        ["BT01", "BT02"]
    )

st.divider()

# ============================================================
# ANALYZE TRIP
# ============================================================

if st.button(
    "🚍 Analyze Trip",
    use_container_width=True
):

    # Check same terminal
    if start_terminal == end_terminal:

        st.error(
            "⚠️ Start and End terminals cannot be the same."
        )

        st.session_state["trip_ready"] = False

    else:

        # Save trip details
        st.session_state["hour"] = hour
        st.session_state["direction"] = direction
        st.session_state["start_terminal"] = start_terminal
        st.session_state["end_terminal"] = end_terminal

        # Mark trip as ready
        st.session_state["trip_ready"] = True

        st.success(
            "✅ Trip details recorded successfully!"
        )

        st.info(
            "🔮 Your trip details are ready for prediction."
        )

# ============================================================
# SELECTED TRIP PREVIEW
# ============================================================

if st.session_state.get("trip_ready", False):

    st.divider()

    st.subheader("📋 Selected Trip")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Starting Hour",
            f"{st.session_state['hour']}:00"
        )

    with col2:
        st.metric(
            "Direction",
            st.session_state["direction"]
        )

    with col3:
        st.metric(
            "From",
            st.session_state["start_terminal"]
        )

    with col4:
        st.metric(
            "To",
            st.session_state["end_terminal"]
        )

