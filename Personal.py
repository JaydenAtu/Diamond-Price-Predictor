import pickle
import streamlit as st

# Load model and scaler
scaler = pickle.load(open('scaler.pkl', 'rb'))
model = pickle.load(open('DModel.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Diamond Price Predictor", layout="wide")

# Custom styles
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Serif&display=swap');

    html, body, [class*="css"] {
        font-family: 'Roboto Serif', serif;
    }

    .stApp {
        background-image: linear-gradient(to bottom right, #35647a, #160c22);;
        background-attachment: fixed;
    }

    div[data-baseweb="select"] {
        background-color: #072629 !important;
        border-radius: 10px !important;
        padding: 8px !important;
        border: 1px solid #0a2328 !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #095e81 !important;
        color: #e1e0e4 !important;
        font-weight: 500;
    }

    div[data-baseweb="popover"] {
        background-color: #095e81 !important;
        color: #e1e0e4 !important;
    }

    div[data-baseweb="option"] {
        background-color: #095e81 !important;
        color: #222 !important;
    }

    div[data-baseweb="option"]:hover {
        background-color: #fcd9b8 !important;
    }
    </style>
""", unsafe_allow_html=True)
# Logo + Title
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("Radiant Riches.png", width=100)
with col_title:
    st.markdown("""
        <h1 style='color: #0bdbd4;'>💎Diamond Price Predictor💎</h1>
        <h4 style='color: #e1e0e4;'>Know the price of your diamond with Radiant Riches' state of the art prediction model</h4>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])

with center:
    st.image("https://images-aka.zalesoutlet.com/education/diamond_anatomy_m.jpg", caption="Anatomy of a Diamond", width = 350)



# Two-column layout: inputs (left), result + gif (right)
input_col, output_col = st.columns([2, 2])

with input_col:
    st.markdown("### 💎 Diamond Specifications")

    # Dropdowns
    cut_list = ["Fair", "Good", "Very Good", "Premium", "Ideal"]
    cut_idx = [0, 1, 4, 3, 2]
    color_list = ['J', 'I', 'H', 'G', 'F', 'E', 'D']
    color_idx = [6, 5, 4, 3, 2, 1, 0]
    clarity_list = ["I1", "SI2", "SII", "VS2", "VS1", "VVS2", "VVS1", "IF"]
    clarity_idx = [0, 3, 2, 5, 4, 7, 6, 1]

    cut = st.selectbox(' Cut Quality', cut_list)
    color = st.selectbox(' Diamond Color', color_list)
    clarity = st.selectbox(' Clarity Grade', clarity_list)

    # Sliders
    st.markdown("### 💎 Physical Dimensions")
    carat = st.slider(' Weight of the Diamond (carats)', 0.20, 5.00, 0.20, 0.01)
    x = st.slider(' Length (mm)', 0.01, 10.74, 0.01, 0.01)
    y = st.slider(' Width (mm)', 0.01, 58.90, 0.01, 0.01)
    z = st.slider(' Depth (mm)', 0.01, 31.80, 0.01, 0.01)

    # Prediction button
    predict = st.button(' Predict Price')

with output_col:
    st.markdown("### 💎 Prediction Result")

    if predict:
        # Prepare and scale input
        X = [
            float(carat),
            float(x),
            float(y),
            float(z),
            int(cut_idx[cut_list.index(cut)]),
            int(color_idx[color_list.index(color)]),
            int(clarity_idx[clarity_list.index(clarity)])
        ]
        X_scaled = scaler.transform([X])
        price = model.predict(X_scaled)

        # Show result
        st.markdown(f"""
            <div style='text-align:center; background-color:#072629; padding:20px; border-radius:10px;'>
                <h2 style='color:#e1e0e4;'> Estimated Price</h2>
                <h1 style='color:#48e4d7;'>${int(price[0]):,}</h1>
            </div>
        """, unsafe_allow_html=True)

        # GIF
        st.image(
            "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHR6N3BmYWk1NjFnbTAycmY4bzZhZWV2ZjYxMmV3OWxyd3E2a2NiYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/46rXT61bNDxAc/giphy.gif",
            caption="Your diamond sparkles bright!",
            use_container_width=True
        )
