# 💎 Diamond Price Prediction App

An end-to-end Machine Learning project and interactive Streamlit web application that estimates diamond prices based on physical attributes and quality metrics.

## 📌 Overview
Determining diamond value relies on complex interactions between physical characteristics (carat, dimensions) and quality metrics (cut, color, clarity). This project cleans, explores, and models diamond data to build an accurate predictive regression model, deployed with a custom Streamlit user interface.

## 🛠️ Tech Stack & Libraries
* **Language:** Python
* **Machine Learning:** Scikit-Learn
* **Data Processing & Analysis:** Pandas, NumPy
* **Visualization & UI:** Streamlit, Matplotlib, Custom CSS

## 📊 Dataset & Model Artifacts
* **Dataset:** The model was trained on the standard Diamonds dataset (attributes including `carat`, `cut`, `color`, `clarity`, `depth`, `table`, `x`, `y`, `z`).
* **Note on Files:** Large data binaries (`diamonds.csv`, `DModel.pkl`, `scaler.pkl`) are omitted from version control to adhere to repository size best practices. You can obtain the raw dataset from [Kaggle's Diamonds Dataset](https://www.kaggle.com/datasets/shivam2503/diamonds).

## 🚀 Key Features
* **Machine Learning Pipeline:** Data preprocessing, feature scaling, and regression modeling evaluated in Jupyter Notebook (`model_training.ipynb`).
* **Interactive UI:** Streamlit dashboard (`Personal.py`) featuring custom styled components for real-time price estimation.

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/JaydenAtu/diamond-price-predictor.git](https://github.com/JaydenAtu/diamond-price-predictor.git)
   cd diamond-price-predictor

2. Install dependencies:
Bash
pip install streamlit scikit-learn pandas numpy matplotlib

3. Train the model or place trained binaries:
Run model_training.ipynb to generate DModel.pkl and scaler.pkl in the root folder.

4. Launch the Streamlit app:
Bash
streamlit run Personal.py

