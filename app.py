import streamlit as st
import joblib
import numpy as np
import pandas as pd
from styles import load_css

model    = joblib.load('model/model.pkl')
scaler   = joblib.load('model/scaler.pkl')
features = joblib.load('model/features.pkl')

st.set_page_config(page_title='House Price Predictor', page_icon='🏠', layout='centered')
st.markdown(load_css(), unsafe_allow_html=True)

st.markdown("""
<div class="hero">
  <div class="hero-tag">AI-Powered Estimator</div>
  <h1>House <span>Price</span> Predictor</h1>
  <p>Get an instant estimate based on size, layout, and room details.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('''<div class="section-label">
    <div class="line"></div><span>Square Footage</span><div class="line"></div>
</div>''', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    gr_liv_area  = st.number_input('Above-grade Living Area (sq ft)', min_value=0, value=1500)
    first_flr_sf = st.number_input('First Floor (sq ft)', min_value=0, value=800)
with col2:
    total_bsmt_sf = st.number_input('Basement Area (sq ft)', min_value=0, value=800)
    second_flr_sf = st.number_input('Second Floor (sq ft)', min_value=0, value=700)

st.markdown('''<div class="section-label">
    <div class="line"></div><span>Rooms</span><div class="line"></div>
</div>''', unsafe_allow_html=True)
col3, col4 = st.columns(2)
with col3:
    bedrooms  = st.slider('Bedrooms', min_value=0, max_value=10, value=3)
    full_bath = st.slider('Full Bathrooms', min_value=0, max_value=5, value=2)
with col4:
    tot_rms        = st.slider('Total Rooms Above Grade', min_value=0, max_value=15, value=7)
    bsmt_full_bath = st.slider('Basement Full Bathrooms', min_value=0, max_value=3, value=0)

half_bath = st.slider('Half Bathrooms', min_value=0, max_value=3, value=0)

st.divider()

if st.button('Predict Price', use_container_width=True, type='primary'):
    sample = pd.DataFrame([{
        'GrLivArea'   : gr_liv_area,
        'TotalBsmtSF' : total_bsmt_sf,
        '1stFlrSF'    : first_flr_sf,
        '2ndFlrSF'    : second_flr_sf,
        'BedroomAbvGr': bedrooms,
        'FullBath'    : full_bath,
        'HalfBath'    : half_bath,
        'BsmtFullBath': bsmt_full_bath,
        'TotRmsAbvGrd': tot_rms,
        'TotalSqFt'   : gr_liv_area + total_bsmt_sf,
        'TotalBaths'  : full_bath + 0.5 * half_bath + bsmt_full_bath
    }])

    log_pred = model.predict(scaler.transform(sample[features]))
    price    = np.expm1(log_pred)[0]

    st.markdown(f"""
        <div class="result-box">
            <div class="label">Predicted Sale Price</div>
            <div class="price">${price:,.0f}</div>
            <div class="sub">Based on the inputs provided</div>
        </div>
    """, unsafe_allow_html=True)