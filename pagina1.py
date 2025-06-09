###################################################
#         Control de eventos sociales             #
# V.0.0.0 //06 06 2025//                          #
# V.1.0.0 //08 06 2025//                          #
# Desplegado con streamlit                        #
# Desarrollador: Sergio Emiliano López Bautista   #
###################################################

import streamlit as st

st.set_page_config(
    page_title="Diana y Emiliano", 
    layout="wide"
)

st.audio("luces.mp3", format="audio/mpeg", loop=True, autoplay=False)
st.image("invitacion.png", caption="prueba 1")