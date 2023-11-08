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

#Import podataka
df1 = pd.read_excel('Mapping of services.xlsx', sheet_name='Administrativni postupci')
df1['Kategorija'] = 'Administrativni postupci'
df2 = pd.read_excel('Mapping of services.xlsx', sheet_name='Diskrecione usluge')
df2['Kategorija'] = 'Diskrecione usluge'
df3 = pd.read_excel('Mapping of services.xlsx', sheet_name='Neinstitucionalizirana prava')
df3['Kategorija'] = 'Neinstitucionalizirana prava'

#Spajanje u jedan dataframe
df = pd.concat([df1,df2,df3], ignore_index=True)

#Transformacije
df['Tip usluge/prava/benefita'] = df['Tip usluge/prava/benefita'].fillna('Nepoznato')
df.rename(columns={"Tip usluge/prava/benefita": "Usluga","Životna dob":"Životna_dob"}, inplace=True)


df['Životna_dob2'] = df['Životna_dob'].str.lower()
df['Životna_dob2'] = df['Životna_dob2'].str.split('; ')

df[['Opis','Ministartvo/Organizacija','Adresa','Web stranica','Telefon','Email','Pravni osnov','Proces aplikacije','Lista neophodnih dokumenata','Link za informacije o prijavi','Dodatne napomene']] = df[['Opis','Ministartvo/Organizacija','Adresa','Web stranica','Telefon','Email','Pravni osnov','Proces aplikacije','Lista neophodnih dokumenata','Link za informacije o prijavi','Dodatne napomene']]. fillna('')


st.write(df)

zd_niz = []
for index, row in df.iterrows():
    try:
        for x in row['Životna_dob2']:
            zd_niz.append(x)
    except:
        pass

zd1 = list(set(zd_niz))

zd = []
for x in zd1:
    a = x[0].upper()+x[1:]
    zd.append(a)
zd.append('Sve')

st.write(zd)
usluge = list(set(df['Usluga'].unique()))
usluge.append('Sve')

st.write(usluge)

#Filteri
col1, col2 = st.columns(2)
with col1:
    zivotna_dob = st.selectbox('Odaberite životnu dob:',options=zd,placeholder='Izaberi neku od opcija', index=5)

with col2:
    usluga = st.selectbox('Odaberite Tip usluge/prava/benefita:',options=usluge,placeholder='Izaberi neku od opcija', index=8)

#Lokacija
lat = 43.853370
lon = 18.385550

data = [[43.853370, 18.385550, "Zavod zdravstvenog osiguranja Kantona Sarajevo", "Ložionička 2", "Sarajevo"]]
map_data = pd.DataFrame(data, columns=['lat', 'lon', 'Naziv', 'Adresa', 'Grad'])

#Filtriranje dataframe-a
if usluga == 'Sve':
    dff = df
else:
    dff = df.query("Usluga == '"+str(usluga)+"'")

if zivotna_dob == 'Sve':
    pass
else:
    #dff2 = dff[dff['Životna_dob2'].apply(lambda x: zivotna_dob.lower() in x)]
    dff = dff.dropna(subset=['Životna_dob2']). \
        loc[dff['Životna_dob2'].apply(lambda x: isinstance(x, list) and zivotna_dob.lower() in x)]
st.write(dff)