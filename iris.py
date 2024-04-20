import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title = "Iris",
    layout = "wide",
)

st.title("Iris Data Analysis")

with st.sidebar:
    st.title('🌸 Iris categorical data')
    st.markdown("<p style='font-weight: bold;'>Choose species</p>", unsafe_allow_html=True)
    check_setosa = st.checkbox("Iris-setosa", value=True)
    check_versicolor = st.checkbox("Iris-versicolor", value=True)
    check_virginica = st.checkbox("Iris-virginica", value=True)
    
    species = []
    if check_setosa:
        species.append("Iris-setosa")
    if check_versicolor:
        species.append("Iris-versicolor")
    if check_virginica:
        species.append("Iris-virginica")
        
    st.markdown("<p style='font-weight: bold;'>Choose variable</p>", unsafe_allow_html=True)
    var1 = st.radio("Main Variables", ("sepal_length", "sepal_width", "petal_length", "petal_width"))
    var2 = st.radio("Secondary Variables", ("sepal_length", "sepal_width", "petal_length", "petal_width"), index=2)
    
data = pd.read_csv("./iris.csv")
data = data.query('species in @species')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.dataframe(data)

with col2:
    fig_scatter = px.scatter(data, x=var1, y=var2, color="species")
    st.plotly_chart(fig_scatter, use_container_width=True)

    
with col3:
	fig_box = px.box(data, x=var1, color='species')
	st.plotly_chart(fig_box, use_container_width=True)
    
with col4:
    fig_pie = px.pie(data, names="species")
    st.plotly_chart(fig_pie, use_container_width=True)
        
st.markdown("<p style='text-align: center;'>Created on 20th April 2024 © Marsetio Noorprajuda. All rights reserved.</p>", unsafe_allow_html=True)