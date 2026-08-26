import streamlit as st
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Prediction Result",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# CUSTOM THEME
# ============================================================

st.markdown("""
<style>

* {
    box-sizing: border-box;
}

/* ================= SIDEBAR ================= */

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


/* ================= MAIN PAGE ================= */

.main-title {
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 5px;
    color: white !important;
}

.main-subtitle {
    font-size: 17px;
    color: #D1D5DB !important;
    margin-bottom: 25px;
}

/* ================= TRIP SUMMARY CARDS ================= */

.summary-card {
    background: #181A21;
    border: 2px solid #555B68;
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    min-height: 115px;
}

.summary-label {
    font-size: 14px;
    color: #FFFFFF;
    margin-bottom: 8px;
}

.summary-value {
    font-size: 28px;
    font-weight: 750;
    color: #FFFFFF;
}


/* ================= PREDICTION CARDS ================= */

.prediction-card {
    background: linear-gradient(
        145deg,
        #191C24,
        #121419
    );

    border: 2px solid #555B68;
    border-radius: 18px;
    padding: 25px;
    min-height: 155px;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.18);

    transition: transform 0.2s ease;
}

.prediction-card:hover {
    transform: translateY(-3px);
}

.prediction-label {
    font-size: 15px;
    color: #FFFFFF;
    margin-bottom: 12px;
}

.prediction-value {
    font-size: 36px;
    font-weight: 800;
    color: #20C7C0;
}

.prediction-unit {
    font-size: 15px;
    color: #FFFFFF;
}


/* ================= STATUS CARD ================= */

.status-card {
    background: #172A40;
    border: 2px solid #5B7FA3;
    border-radius: 16px;
    padding: 20px 25px;
    font-size: 17px;
    color: #FFFFFF;
}

.status-card b {
    color: #FFFFFF;
}


/* ================= EXPLANATION CARD ================= */

.explanation-card {
    background: #181A21;
    border: 2px solid #555B68;
    border-radius: 16px;
    padding: 22px;
    font-size: 16px;
    line-height: 1.6;
    color: #FFFFFF;
}

.explanation-card b {
    color: #20C7C0;
}


/* ================= SECTION TITLE ================= */

.section-title {
    font-size: 25px;
    font-weight: 750;
    margin-top: 8px;
    margin-bottom: 18px;
    color: white !important;
}
/* ================= DIVIDER ================= */

.custom-divider {
    height: 1px;
    background: #30343E;
    margin: 30px 0;
}


/* ================= MOBILE RESPONSIVE ================= */



@media (max-width: 768px) {

    .main-title {
        font-size: 30px;
        line-height: 1.2;
        color: white !important;
    }

    .main-subtitle {
        font-size: 15px;
        line-height: 1.5;
        color: #D1D5DB !important;
    }

    .section-title {
        font-size: 21px;
        color: white !important;
    }

}
    .summary-card {
        min-height: 100px;
        padding: 15px;
        border-width: 2px;
    }

    .summary-label {
        font-size: 13px;
        color: #FFFFFF !important;
    }

    .summary-value {
        font-size: 23px;
        color: #FFFFFF !important;
    }

    .prediction-card {
        min-height: 130px;
        padding: 18px;
        border-width: 2px;
    }

    .prediction-label {
        font-size: 14px;
        color: #FFFFFF !important;
    }

    .prediction-value {
        font-size: 30px;
    }

    .prediction-unit {
        font-size: 14px;
        color: #FFFFFF !important;
    }

    .status-card {
        padding: 17px;
        font-size: 15px;
        border: 2px solid #6E91B5;
        color: #FFFFFF !important;
    }

    .status-card b {
        color: #FFFFFF !important;
    }

    .explanation-card {
        padding: 18px;
        font-size: 15px;
        line-height: 1.55;
        border: 2px solid #626875;
        color: #FFFFFF !important;
    }

    .explanation-card b {
        color: #20C7C0 !important;
    }

}


/* ================= STREAMLIT MOBILE FIX ================= */

@media (max-width: 480px) {

    .summary-card {
        margin-bottom: 10px;
    }

    .prediction-card {
        margin-bottom: 10px;
    }

    .status-card,
    .explanation-card {
        width: 100%;
        overflow-wrap: break-word;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CHECK TRIP INPUT
# ============================================================

if "trip_ready" not in st.session_state or not st.session_state["trip_ready"]:

    st.warning(
        "⚠️ Please enter and analyze a trip from the Trip Input page first."
    )

    st.stop()


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
# PREPARE ML DATA
# ============================================================

X = df[
    [
        "hour",
        "direction",
        "start_terminal",
        "end_terminal"
    ]
]

y = df["duration_in_mins"]

X = pd.get_dummies(
    X,
    columns=[
        "start_terminal",
        "end_terminal"
    ],
    dtype=int
)


# ============================================================
# TRAIN / TEST SPLIT
# ============================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ============================================================
# RANDOM FOREST
# ============================================================

rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(
    X_train,
    y_train
)


# ============================================================
# LINEAR REGRESSION
# ============================================================

linear_model = LinearRegression()

linear_model.fit(
    X_train,
    y_train
)


# ============================================================
# GET USER INPUT
# ============================================================

hour = st.session_state["hour"]
direction = st.session_state["direction"]
start_terminal = st.session_state["start_terminal"]
end_terminal = st.session_state["end_terminal"]


# ============================================================
# CONVERT USER INPUT
# ============================================================

start_bt01 = 1 if start_terminal == "BT01" else 0
start_bt02 = 1 if start_terminal == "BT02" else 0

end_bt01 = 1 if end_terminal == "BT01" else 0
end_bt02 = 1 if end_terminal == "BT02" else 0


new_data = pd.DataFrame(
    [[
        hour,
        direction,
        start_bt01,
        start_bt02,
        end_bt01,
        end_bt02
    ]],
    columns=X.columns
)


# ============================================================
# PREDICTIONS
# ============================================================

rf_prediction = rf_model.predict(new_data)[0]

linear_prediction = linear_model.predict(new_data)[0]


# ============================================================
# HISTORICAL ROUTE AVERAGE
# ============================================================

route_data = df[
    (df["start_terminal"] == start_terminal)
    &
    (df["end_terminal"] == end_terminal)
]

if len(route_data) > 0:

    historical_average = (
        route_data["duration_in_mins"].mean()
    )

else:

    historical_average = None


# ============================================================
# SAVE PREDICTION HISTORY
# ============================================================

history_file = "prediction_history.csv"

current_prediction_key = (
    f"{hour}_"
    f"{direction}_"
    f"{start_terminal}_"
    f"{end_terminal}_"
    f"{round(rf_prediction, 2)}"
)


if st.session_state.get("saved_prediction_key") != current_prediction_key:

    new_record = pd.DataFrame([{
        "Starting Hour": f"{hour}:00",
        "Direction": direction,
        "Route": f"{start_terminal} → {end_terminal}",
        "Random Forest": round(rf_prediction, 2),
        "Linear Regression": round(linear_prediction, 2),
        "Historical Average": (
            round(historical_average, 2)
            if historical_average is not None
            else None
        )
    }])

    if os.path.exists(history_file):

        old_history = pd.read_csv(history_file)

    else:

        old_history = pd.DataFrame()


    if not old_history.empty:

        duplicate = old_history[
            (old_history["Starting Hour"] == f"{hour}:00")
            &
            (old_history["Direction"] == direction)
            &
            (old_history["Route"] ==
             f"{start_terminal} → {end_terminal}")
            &
            (old_history["Random Forest"] ==
             round(rf_prediction, 2))
        ]

    else:

        duplicate = pd.DataFrame()


    if duplicate.empty:

        if old_history.empty:

            updated_history = new_record

        else:

            updated_history = pd.concat(
                [old_history, new_record],
                ignore_index=True
            )

        updated_history.to_csv(
            history_file,
            index=False
        )


    st.session_state["saved_prediction_key"] = (
        current_prediction_key
    )


# ============================================================
# PREDICTION DASHBOARD
# ============================================================

st.markdown(
    '<div class="main-title">🤖 Trip Prediction Result</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Machine learning based travel-time estimation for the selected trip.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# TRIP SUMMARY
# ============================================================

st.markdown(
    '<div class="section-title">📍 Trip Summary</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-label">🕐 Starting Hour</div>
            <div class="summary-value">{hour}:00</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-label">🧭 Direction</div>
            <div class="summary-value">{direction}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-label">📍 From</div>
            <div class="summary-value">{start_terminal}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        f"""
        <div class="summary-card">
            <div class="summary-label">🏁 To</div>
            <div class="summary-value">{end_terminal}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PREDICTION SECTION
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🚌 Estimated Travel Time</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:

    st.markdown(
        f"""
        <div class="prediction-card">
            <div class="prediction-label">🌲 Random Forest</div>
            <div class="prediction-value">
                {rf_prediction:.2f}
                <span class="prediction-unit">min</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="prediction-card">
            <div class="prediction-label">📈 Linear Regression</div>
            <div class="prediction-value">
                {linear_prediction:.2f}
                <span class="prediction-unit">min</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    if historical_average is not None:

        st.markdown(
            f"""
            <div class="prediction-card">
                <div class="prediction-label">📊 Historical Average</div>
                <div class="prediction-value">
                    {historical_average:.2f}
                    <span class="prediction-unit">min</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="prediction-card">
                <div class="prediction-label">
                    📊 Historical Average
                </div>
                <div class="prediction-value">
                    N/A
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# TRAVEL STATUS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🚦 Travel Time Status</div>',
    unsafe_allow_html=True
)

overall_average = df["duration_in_mins"].mean()


if rf_prediction <= overall_average * 0.90:

    st.markdown(
        """
        <div class="status-card">
            🟢 <b>Low Travel Time</b><br>
            This trip is expected to be faster than normal.
        </div>
        """,
        unsafe_allow_html=True
    )

elif rf_prediction <= overall_average * 1.10:

    st.markdown(
        """
        <div class="status-card">
            🟡 <b>Moderate Travel Time</b><br>
            This trip is close to the normal travel time.
        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="status-card">
            🔴 <b>High Travel Time</b><br>
            This trip is expected to take longer than normal.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PREDICTION EXPLANATION
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">💡 Prediction Summary</div>',
    unsafe_allow_html=True
)


if historical_average is not None:

    difference = rf_prediction - historical_average

    if difference > 0:

        explanation = (
            f"The Random Forest model predicts approximately "
            f"<b>{difference:.2f} minutes longer</b> than the "
            f"historical average for this route."
        )

    elif difference < 0:

        explanation = (
            f"The Random Forest model predicts approximately "
            f"<b>{abs(difference):.2f} minutes shorter</b> than the "
            f"historical average for this route."
        )

    else:

        explanation = (
            "The prediction is approximately equal to the "
            "historical route average."
        )

else:

    explanation = (
        "No historical data is available for this route."
    )


st.markdown(
    f"""
    <div class="explanation-card">
        💬 {explanation}
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HISTORY STATUS
# ============================================================

st.markdown(
    '<div class="custom-divider"></div>',
    unsafe_allow_html=True
)

st.caption(
    "✅ This prediction has been recorded in Prediction History."
)
