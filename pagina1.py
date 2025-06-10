###################################################
#         Control de eventos sociales             #
# V.0.0.0 //06 06 2025//                          #
# V.1.0.0 //08 06 2025//                          #
# Desplegado con streamlit                        #
# Desarrollador: Sergio Emiliano López Bautista   #
###################################################


#--------------------- Requerimientos ---------------------
import os
import codecs
import streamlit as st
import base64
from streamlit.components.v1 import html
from dotenv import load_dotenv, find_dotenv

#---------------------- Estructuras -----------------------

#----------------------- Funciones ------------------------

#----------------------- Seteadores -----------------------
st.set_page_config(
    page_title="Diana y Emiliano", 
    layout="wide",
    page_icon = "💍"
)
dotenv_path = find_dotenv()
load_dotenv(dotenv_path, override=True)
GOOGLE_MAPS_API_KEY = os.getenv("DIEMI_MAPS_API_KEY")
#GOOGLE_MAPS_API_KEY = st.secrets["DIEMI_MAPS_API_KEY"]

#----------------------- Interfaz -------------------------
st.markdown("## ESTO ES SÓLO UNA PRUEBA. NO ES LA INVITACIÓN REAL")
st.audio("luces.mp3", format = "audio/mpeg", loop = True, autoplay = True)
#st.image("invitacion.png", caption="prueba 1")

html("""
<div style="position: relative; width: 100%; height: 0; padding-top: 402.5622%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGp0ojamT0/po2hPZrMdhfGEHm9EOtOkA/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
""", height=1700,scrolling=True)

#Dirección estática
direccion = "Francisco Javier Mina 218, San Mateo, Tláhuac, 13040 Ciudad de México, CDMX, México"

#Crear iframe del mapa
mapa_html = f"""
<iframe
  width="100%"
  height="500"
  style="border:0"
  loading="lazy"
  allowfullscreen
  referrerpolicy="no-referrer-when-downgrade"
  src="https://www.google.com/maps/embed/v1/place?key={GOOGLE_MAPS_API_KEY}&q={direccion.replace(' ', '+')}">
</iframe>
"""

#columnas = st.columns(2)
# Mostrar en la app
st.link_button("Salón Los pinos", "https://maps.app.goo.gl/cKfdKkQjmgZi5bs66")
html(mapa_html,height=500)
#------------------------ MAIN ----------------------------