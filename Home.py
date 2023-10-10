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
    kategorija = st.multiselect('Odaberite kategoriju usluge/prava/benefita:',lista_usluga)

with col2:
    users = st.multiselect('Odaberite kategoriju korisnika:',useri)

df = services.query('Servis == "'+str(kategorija)+'" & Users == "'+str(users)+'"')
st.write(df)


dokumenti = pd.read_excel('Mapping of services.xlsx',sheet_name='Lista potrebnih dokumenata')

"""
## Lista potrebnih dokumenata
"""

st.write(dokumenti)