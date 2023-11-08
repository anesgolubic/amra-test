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
df1['Kategorija'] = 'Administrativni postupci'
df2 = pd.read_excel('Mapping of services.xlsx', sheet_name='Diskrecione usluge')
df2['Kategorija'] = 'Diskrecione usluge'
df3 = pd.read_excel('Mapping of services.xlsx', sheet_name='Neinstitucionalizirana prava')
df3['Kategorija'] = 'Neinstitucionalizirana prava'

st.write(df1)
st.write(df2)
st.write(df3)

df = pd.concat([df1,df2,df3], ignore_index=True)
st.write(df)

df['Tip usluge/prava/benefita'] = df['Tip usluge/prava/benefita'].fillna('Nepoznato')
df.rename(columns={"Tip usluge/prava/benefita": "Usluga","Životna dob":"Životna_dob"}, inplace=True)

df[['Opis','Ministartvo/Organizacija','Adresa','Web stranica','Telefon','Email','Pravni osnov','Proces aplikacije','Lista neophodnih dokumenata','Link za informacije o prijavi','Dodatne napomene']] = df[['Opis','Ministartvo/Organizacija','Adresa','Web stranica','Telefon','Email','Pravni osnov','Proces aplikacije','Lista neophodnih dokumenata','Link za informacije o prijavi','Dodatne napomene']]. fillna('')

zd = df['Životna_dob'].unique()
usluge = df['Usluga'].unique()

#Filteri
col1, col2 = st.columns(2)
with col1:
    zivotna_dob = st.selectbox('Odaberite životnu dob:',zd)

with col2:
    usluga = st.selectbox('Odaberite Tip usluge/prava/benefita:',usluge)