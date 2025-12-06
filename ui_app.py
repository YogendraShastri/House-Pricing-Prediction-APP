import requests
import streamlit as st

API_URL = "http://localhost:8000"  # FastAPI base URL

st.set_page_config(page_title="House Price Predictor", layout="centered")
st.title("🏠 House Price Prediction")

st.subheader("Enter house details")

with st.form("house_form"):
    area = st.number_input("Area (sq ft)", min_value=0.0, value=1000.0, step=10.0)
    bedrooms = st.number_input("Bedrooms", min_value=0, value=3, step=1)
    bathrooms = st.number_input("Bathrooms", min_value=0, value=2, step=1)
    stories = st.number_input("Stories", min_value=0, value=1, step=1)
    parking = st.number_input("Parking spots", min_value=0, value=1, step=1)

    mainroad = st.selectbox("Main road access", ["yes", "no"])
    guestroom = st.selectbox("Guest room", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwaterheating = st.selectbox("Hot water heating", ["yes", "no"])
    airconditioning = st.selectbox("Air conditioning", ["yes", "no"])
    prefarea = st.selectbox("Preferred area", ["yes", "no"])

    furnishingstatus = st.selectbox(
        "Furnishing status",
        ["furnished", "semi-furnished", "unfurnished"],
        index=1,
    )

    submitted = st.form_submit_button("Predict price")

if submitted:
    payload = {
        "area": area,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "stories": stories,
        "parking": parking,
        "mainroad": mainroad,
        "guestroom": guestroom,
        "basement": basement,
        "hotwaterheating": hotwaterheating,
        "airconditioning": airconditioning,
        "prefarea": prefarea,
        "furnishingstatus": furnishingstatus,
    }

    try:
        resp = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            st.success(f"Predicted price: {data['predicted_price']:.2f}")
        else:
            st.error(f"API error {resp.status_code}: {resp.text}")
    except Exception as e:
        st.error(f"Request failed: {e}")