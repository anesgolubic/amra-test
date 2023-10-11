import streamlit as st
st.set_page_config(
    page_title="Amra test",
    #page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

import pandas as pd
from streamlit_modal import Modal
import streamlit.components.v1 as components
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

for index, row in df.iterrows():
    st.markdown('<p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Servis'])+'</p><p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Users'])+'<p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Age'])+'</p>', unsafe_allow_html=True)
    #st.markdown('<p style="margin:0;display:inline;float:left" class="blog-label">'+str(row['Age'])+'</p>', unsafe_allow_html=True)
    #st.markdown('<p style="margin:0;display:inline;float:left" class="blog-label">'+str(row['Users'])+'</p>', unsafe_allow_html=True)
    st.markdown('<h3>'+str(row['Name'])+'</h3>', unsafe_allow_html=True)
    st.markdown('<p>'+str(row['Description'])+'</p>', unsafe_allow_html=True)
    #st.divider()
    #st.write('Government Agency/Organization')
    #st.markdown('<h4>'+str(row['Government Agency/Organization'])+'</h3>', unsafe_allow_html=True)


    modal = Modal(key="Demo Key", title="Government Agency/Organization")
    open_modal = st.button("Government Agency/Organization")
    if open_modal:
        modal.open()

    if modal.is_open():
        with modal.container():
            
            html_string = '''
            <h3>Ministarstvo za rad, socijalnu politiku, raseljena lica i izbjeglice</h3>
            <p>Reisa Džemaludina Čauševića 1</p>
            <p>033/723-635</p>
            <p>mirsada@kcsr.ba</p>
            <a href="https://mrsri.ks.gov.ba/">Website</a>
            '''
            components.html(html_string)

    st.divider()
dokumenti = pd.read_excel('Mapping of services.xlsx',sheet_name='Lista potrebnih dokumenata', skiprows = range(1, 8), header = 1)

"""
## Lista potrebnih dokumenata
"""

st.dataframe(dokumenti)