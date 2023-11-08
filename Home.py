import streamlit as st
st.set_page_config(
    page_title="Amra test",
    #page_icon="🧊",
    layout="wide",
)

import pandas as pd
import plotly.express as px
from streamlit_modal import Modal
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium, folium_static
#from datetime import date, timedelta
#import numpy as np

# LINK TO THE CSS FILE
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)


st.image('UNWomen logo.png')
"""
# Mapa prava i usluga  za osobe sa invaliditetom i starije
"""

df1 = pd.read_excel('Mapping of services.xlsx', sheet_name='Administrativni postupci')
df2 = pd.read_excel('Mapping of services.xlsx', sheet_name='Diskrecione usluge')
df3 = pd.read_excel('Mapping of services.xlsx', sheet_name='Neinstitucionalizirana prava')

st.write(df1)
st.write(df2)
st.write(df3)