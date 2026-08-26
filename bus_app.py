import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="TransitIQ | Bus Travel Analytics",
    page_icon="🚌",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PAGE NAVIGATION
# ============================================================

pages = [
    st.Page(
        "pages/1_Trip_Input.py",
        title="Trip Input",
        icon="📍"
    ),

    st.Page(
        "pages/2_Prediction.py",
        title="Prediction",
        icon="🔮"
    ),

    st.Page(
        "pages/3_Analytics.py",
        title="Analytics",
        icon="📊"
    ),

    st.Page(
        "pages/4_Insights.py",
        title="Insights",
        icon="💡"
    ),

    st.Page(
        "pages/5_Prediction_History.py",
        title="Prediction History",
        icon="🕐"
    )
]


# ============================================================
# HIDE DEFAULT NAVIGATION
# ============================================================

pg = st.navigation(
    pages,
    position="hidden"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* ==========================================================
   SIDEBAR BACKGROUND
========================================================== */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #06413E 0%,
        #075F5A 50%,
        #087A74 100%
    );
}


/* ==========================================================
   SIDEBAR TOP SPACING
========================================================== */

[data-testid="stSidebar"] > div:first-child {
    padding-top: 20px;
}


/* ==========================================================
   TRANSITIQ BRAND
========================================================== */

.transitiq-brand {
    background: linear-gradient(
        135deg,
        #20B9B2,
        #19AAA5
    );

    border-radius: 14px;

    padding: 14px 18px;

    margin: 0 10px 18px 10px;

    font-size: 24px;

    font-weight: 800;

    letter-spacing: 1px;

    color: white;

    text-align: center;

    box-shadow:
        0 4px 12px rgba(0,0,0,0.22);
}


/* ==========================================================
   NAVIGATION ITEM SPACING
========================================================== */

.nav-item {
    margin: 1px 10px !important;
}


/* ==========================================================
   NAVIGATION LINKS
========================================================== */

[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {

    border-radius: 10px !important;

    padding: 7px 12px !important;

    margin: 0 !important;

    min-height: 0 !important;

    font-size: 16px !important;

    font-weight: 600 !important;

    color: white !important;

    transition: all 0.2s ease;
}


/* ==========================================================
   HOVER EFFECT
========================================================== */

[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {

    background-color: rgba(32,185,178,0.30) !important;

    transform: translateX(3px);
}


/* ==========================================================
   ACTIVE PAGE
========================================================== */

[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"][aria-current="page"] {

    background-color: rgba(32,185,178,0.35) !important;

    border-left: 4px solid #20CFC7 !important;

    font-weight: 700 !important;
}


/* ==========================================================
   SIDEBAR TEXT
========================================================== */

[data-testid="stSidebar"] * {
    color: white;
}


/* ==========================================================
   REMOVE DEFAULT STREAMLIT NAVIGATION
========================================================== */

[data-testid="stSidebarNav"] {
    display: none !important;
}


/* ==========================================================
   MAIN TITLE
========================================================== */

.main-title {
    font-size: 42px;
    font-weight: 750;
    margin-bottom: 5px;
}


/* ==========================================================
   SUBTITLE
========================================================== */

.subtitle {
    font-size: 18px;
    opacity: 0.70;
    margin-bottom: 25px;
}


/* ==========================================================
   SECTION TITLE
========================================================== */

.section-title {
    font-size: 27px;
    font-weight: 700;
    margin-top: 10px;
}


/* ==========================================================
   INFO CARD
========================================================== */

.info-card {
    padding: 20px;

    border-radius: 14px;

    border-left: 5px solid #20B9B2;

    border-top: 1px solid rgba(32,185,178,0.25);

    border-right: 1px solid rgba(32,185,178,0.25);

    border-bottom: 1px solid rgba(32,185,178,0.25);

    margin-bottom: 15px;
}


/* ==========================================================
   FEATURE CARD
========================================================== */

.feature-card {
    padding: 22px;

    border-radius: 14px;

    border: 1px solid rgba(32,185,178,0.25);

    border-top: 4px solid #20B9B2;

    min-height: 150px;

    margin-bottom: 18px;
}


/* ==========================================================
   FOOTER
========================================================== */

.footer {
    text-align: center;

    opacity: 0.60;

    padding: 25px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# CUSTOM SIDEBAR
# ============================================================

with st.sidebar:

    # --------------------------------------------------------
    # TRANSITIQ BRAND
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="transitiq-brand">
            🚍 TRANSITIQ
        </div>
        """,
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # TRIP INPUT
    # --------------------------------------------------------

    st.markdown(
        '<div class="nav-item">',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/1_Trip_Input.py",
        label="Trip Input",
        icon="📍"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # PREDICTION
    # --------------------------------------------------------

    st.markdown(
        '<div class="nav-item">',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/2_Prediction.py",
        label="Prediction",
        icon="🔮"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # ANALYTICS
    # --------------------------------------------------------

    st.markdown(
        '<div class="nav-item">',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/3_Analytics.py",
        label="Analytics",
        icon="📊"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # INSIGHTS
    # --------------------------------------------------------

    st.markdown(
        '<div class="nav-item">',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/4_Insights.py",
        label="Insights",
        icon="💡"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # PREDICTION HISTORY
    # --------------------------------------------------------

    st.markdown(
        '<div class="nav-item">',
        unsafe_allow_html=True
    )

    st.page_link(
        "pages/5_Prediction_History.py",
        label="Prediction History",
        icon="🕐"
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# RUN SELECTED PAGE
# ============================================================

pg.run()
