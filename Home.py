import streamlit as st
st.set_page_config(
    page_title="Amra test",
    #page_icon="🧊",
    #layout="wide",
    initial_sidebar_state="expanded",
)

import pandas as pd
from datetime import date, timedelta
import numpy as np

# LINK TO THE CSS FILE
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

"""
# Amra test
## Neki podnaslov
"""

services = pd.read_excel('Mapping of services.xlsx',sheet_name='Mapiranje usluga')
services['Servis'] = services['Type of Service/Right/Benefit']
lista_usluga = services['Servis'].unique()
useri =  services['Users'].unique()

col1, col2 = st.columns(2)
with col1:
    kategorija = st.selectbox('Odaberite kategoriju usluge/prava/benefita:',lista_usluga)

with col2:
    users = st.selectbox('Odaberite kategoriju korisnika:',useri)

df = services.query('Servis == "'+str(kategorija)+'" & Users == "'+str(users)+'"')
st.write(df)

true_html = '<input type="checkbox" checked disabled="true">'

test = '<section class="blog-card"><div class="blog-content"><p class="blog-label">Technology</p><h1>Lorem ipsum dolor sit amet.</h1><p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Voluptatem aliquid sunt temporibus repellendus neque, quibusdam exercitationem.</p></div></section>'

st.markdown(test, unsafe_allow_html=True)


dokumenti = pd.read_excel('Mapping of services.xlsx',sheet_name='Lista potrebnih dokumenata', skiprows = range(1, 8), header = 1)

"""
## Lista potrebnih dokumenata
"""

st.dataframe(dokumenti)