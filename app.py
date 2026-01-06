import streamlit as st
import pandas as pd
import plotly.express as px
import time 

# 1. Page Configuration
st.set_page_config(
    page_title="RISKLY | AI Audit & Risk Management",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Global CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0rem;
        border-bottom: 1px solid #333;
        margin-bottom: 3rem;
    }
    .logo {
        font-size: 26px;
        font-weight: 800; 
        color: #4DB6AC; 
    }
    .nav-links {
        display: flex; gap: 30px; color: #A0A0A0; font-weight: 500; font-size: 14px;
    }
    .nav-links a {
        color: #A0A0A0;
        text-decoration: none;
        transition: 0.3s;
    }
    .nav-links a:hover {
        color: #4DB6AC;
    }
    div.stButton > button:first-child {
        background-color: #FF4B4B !important;
        color: white !important;
        border: none !important;
        padding: 15px 40px !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        margin-top: 10px !important; 
    }
    [data-testid="stFileUploader"] {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
    }
    [data-testid="stMetricValue"] {
        font-size: 26px !important;
        color: white;
        font-weight: 700;
    }
    </style>
    
    <div class="navbar">
        <div class="logo">RISKLY.</div>
        <div class="nav-links">
            <a href="https://www.linkedin.com/in/christian-reveles-373095324/" target="_blank">LINKEDIN</a>
            <a href="https://uark.joinhandshake.com/profiles/christianreveles" target="_blank">HANDSHAKE</a>
            <a href="#about-me">ABOUT ME</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 3. Hero Section
col1, col2 = st.columns([1.5, 1]) 

with col1:
    st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
    st.markdown("""
    <h1 style='font-size: 54px; font-weight: 800; color: white; line-height: 1.2; margin-bottom: 20px;'>
    Control & Risk Intelligence
    </h1>
    """, unsafe_allow_html=True)
    st.markdown("""
    <p style='font-size: 20px; color: #B0B0B0; margin-bottom: 40px; line-height: 1.5; max-width: 800px;'>
    Connect, analyze, and transform audit data into actionable insights with Riskly’s AI risk intelligence platform.
    </p>
    """, unsafe_allow_html=True)
    st.button("Get Started Now")

with col2:
    # Reliable high-tech professional image
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000", use_container_width=True)

# 4. Interactive Dashboard Section
st.markdown("---")
st.markdown("### Interactive Risk Simulator")

dash_col1, dash_col2 = st.columns([1, 2])

with dash_col1:
    st.markdown("#### 1. Upload Financial Data")
    st.caption("Upload your ledger (CSV/XLSX) to trigger AI analysis.")
    uploaded_file = st.file_uploader("Upload Audit Trail", type=['csv', 'xlsx'])

    if uploaded_file is None:
        st.info("👆 Upload a file to see the risk analysis.")

with dash_col2:
    if uploaded_file is not None:
        with st.spinner('🤖 AI is scanning for anomalies...'):
            time.sleep(2) 
        
        simulated_data = pd.DataFrame({
            'Risk_Category': ['Fraud', 'Compliance', 'Operational', 'Liquidity', 'Market'],
            'Risk_Score': [92, 45, 20, 35, 88], 
            'Status': ['Critical', 'Stable', 'Safe', 'Stable', 'Critical']
        })
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Avg Risk Score", "76.4", delta="+12.5")
        m2.metric("Critical Anomalies", "2", delta="Immediate Action", delta_color="inverse")
        m3.metric("Audit Status", "ACTION REQUIRED", "Flagged")

        st.markdown("#### Real-time Risk Assessment")
        fig = px.bar(
            simulated_data, 
            x='Risk_Category', 
            y='Risk_Score', 
            color='Status', 
            color_discrete_map={'Critical':'#FF4B4B', 'Stable':'#00E676', 'Safe':'#2979FF'}, 
            template="plotly_dark"
        )
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", height=350)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.markdown("<div style='border: 2px dashed #333; border-radius: 10px; height: 300px; display: flex; align-items: center; justify-content: center; color: #555;'><i>Chart will appear here after upload</i></div>", unsafe_allow_html=True)

# 5. About Me Section
st.markdown("<div id='about-me'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("### About the Developer")

about_col1, about_col2 = st.columns([1, 2.5])

with about_col1:
    # Professional analyst photo
    st.image("https://images.unsplash.com/photo-1560179707-f14e90ef3623?auto=format&fit=crop&q=80&w=800", use_container_width=True)

with about_col2:
    st.markdown(f"""
    **Hi, my name is Christian Reveles.**
    
    I am the developer behind **RISKLY**. My mission in creating this platform was to help audit and risk professionals 
    bridge the gap between complex financial data and actionable insights using AI-driven intelligence. 
    
    As a student at the **University of Arkansas**, I built this simulator to demonstrate how modern technology 
    can automate the detection of critical anomalies, allowing human experts to focus on high level strategy 
    rather than manual data sorting.
    
    I am passionate about using Python and modern data visualization to make complex risks easy to 
    understand at a glance.
    
    **Connect with me:**
    * [LinkedIn Profile](https://www.linkedin.com/in/christian-reveles-373095324/)
    * [Handshake Profile](https://uark.joinhandshake.com/profiles/christianreveles)
    """)