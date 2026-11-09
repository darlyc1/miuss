#creacion de pagina uss
import streamlit as st
#lado izquierdo
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.header("¡Hola, Barra Lateral!")
st.sidebar.text("Esto es una barra lateral")
st.sidebar.image("C:\Users\miyi2\Downloads\logo_uss..jpeg")
st.sidebar.button("Haz clic pero en la barra lateral")
texto_barra = st.sidebar.text_input("Escribe algo en la barra:")
st.sidebar.write("Escribiste en la barra:", texto_barra)
#lado derecho
st.title("Mi primera aplicación de Streamlit")
st.header("¡Hola, Streamlit!")
st.text("Esta es una aplicación simple")
st.image("C:\Users\miyi2\Downloads\logo_uss..jpeg")
st.button("Haz clic")
texto = st.text_input("Escribe algo:")
st.write("Escribiste:", texto)

pip install streamlit
streamlit run app.py