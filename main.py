#################### Files Required For Deployment ################################

# UI : implemented by python streamlit library
# Trained Model Files: Saved pkl files
# Logic Code connecting UI & Pkl files

################# UI ##########################
import streamlit as st  # pip install streamlit

st.markdown("""<style>.stApp {background-image: url('https://images.unsplash.com/photo-1593190910427-b949baf80788?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D""", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: DeepPink;'>Water Quality Index</h1>", unsafe_allow_html=True)
cola, colb, colc = st.columns(3)
with colb:
    st.image("C:\\Users\\Saiku\\Downloads\\Deploy Streamlit\\Children-Water-.jpg")
    st.image("C:\\Users\\Saiku\\Downloads\\Deploy Streamlit\\subsampling-2_gettyimages-_Gill.jpeg")

st.write("Predictive Model Built on Below Sample Data")

import pandas as pd

df = pd.read_csv("water_potability.csv")

st.dataframe(df.tail())

# Taking X column values from user

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input(f"Enter ph Value Min {df.ph.min()} to Max {df.ph.max()}")

with col2:
    Hardness = st.number_input(f"Enter Hardness Value Min {df.Hardness.min()} to Max {df.Hardness.max()}")

col3, col4 = st.columns(2)

with col3:
    Solids = st.number_input(f"Enter Solids Value Min {df.Solids.min()} to Max {df.Solids.max()}")

with col4:
    Chloramines = st.number_input(f"Enter Chloramines Value Min {df.Chloramines.min()} to Max {df.Chloramines.max()}")

col5, col6 = st.columns(2)
with col5:
    Sulfate = st.number_input(f"Enter Sulfate Value Min {df.Sulfate.min()} to Max {df.Sulfate.max()}")

with col6:
    Conductivity = st.number_input(f"Enter Conductivity Value Min {df.Conductivity.min()} to Max {df.Conductivity.max()}")

col7, col8 = st.columns(2)
with col7:
    Organic_carbon = st.number_input(f"Enter Organic_carbon Value Min {df.Organic_carbon.min()} to Max {df.Organic_carbon.max()}")

with col8:
    Trihalomethanes = st.number_input(f"Enter Trihalomethanes Value Min {df.Trihalomethanes.min()} to Max {df.Trihalomethanes.max()}")
Turbidity = st.number_input(f"Enter Turbidity Value Min {df.Turbidity.min()} to Max {df.Turbidity.max()}")

xdata = [ph,Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon,Trihalomethanes,Turbidity]
###################### Writing Prediction Logic ######################

# Loading model

import pickle

with open('water_naive.pkl', 'rb') as f:
    model = pickle.load(f)

x = pd.DataFrame([xdata], columns=df.columns[0:9])

st.write("Given Input:")
st.dataframe(x)

if st.button("Predict"):
    prediction = model.predict(x)

    if prediction[0] == 0:
        st.markdown("<h1 style='text-align: center; color: red;'>Water is Unsafe for Drinking</h1>",
                    unsafe_allow_html=True)
    elif prediction[0] == 1:
        st.markdown("<h1 style='text-align: center; color: blue;'>Water is safe for Drinking</h1>", unsafe_allow_html=True)
    else:
        st.write('Unknown label')
        st.markdown("<h1 style='text-align: center; color: yellow;'>Unknown label</h1>",
                    unsafe_allow_html=True)

