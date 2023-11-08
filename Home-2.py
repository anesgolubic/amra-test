


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

df = pd.read_excel('Mapping of services.xlsx', sheet_name='All')

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

#Lokacija
lat = 43.853370
lon = 18.385550

data = [[43.853370, 18.385550, "Zavod zdravstvenog osiguranja Kantona Sarajevo", "Ložionička 2", "Sarajevo"]]
map_data = pd.DataFrame(data, columns=['lat', 'lon', 'Naziv', 'Adresa', 'Grad'])

#Filtriranje dataframe-a
dff = df.query("Životna_dob == '"+str(zivotna_dob)+"' & Usluga == '"+str(usluga)+"'")

for index,row in dff.iterrows():
    with st.expander(row['Naziv ']):
        st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
        st.markdown('<p style="margin-top:10px;display:inline;float:left" class="blog-label">'+str(row['Usluga'])+'</p><p style="margin-left:5px;margin-top:10px;display:inline;float:left" class="blog-label">'+str(row['Životna_dob'])+'</p>', unsafe_allow_html=True)
        st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)

        col1, col2 = st.columns([1,3])
        with col1:
            st.markdown('<h5>Pravo:</h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Pravo'])+'</p>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h5>Pravni osnov:</h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Pravni osnov'])+'</p>', unsafe_allow_html=True)

        st.divider()

        tab1, tab2, tab3 = st.tabs(["Ministarstvo/Organizacija", "Proces aplikacije", "Dodatne napomene"])
        with tab1:
            st.markdown('<h5>'+str(row['Ministartvo/Organizacija'])+'</h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Adresa'])+'</p>', unsafe_allow_html=True)
            st.markdown('<a href="+'+str(row['Web stranica'])+'">'+str(row['Web stranica'])+'</a>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Telefon'])+'</p>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Email'])+'</p>', unsafe_allow_html=True)

            fig = px.scatter_mapbox(map_data, lat="lat", lon="lon", zoom=17, height=300, hover_name="Naziv",
                                    hover_data=["Adresa","Grad"],)
            fig.update_layout(mapbox_style="carto-positron")
            fig.update_traces(marker={'size': 15})
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig, use_container_width=True, config=dict(
                displayModeBar=False))

            #mapa = pd.DataFrame({
            #"lat": [43.853370],
            #"lon": [18.385550]
            #})
            #st.map(mapa,
            #latitude='lat',
            #longitude='lon', zoom=17, size=5)
        with tab2:
            st.markdown('<h5>Proces aplikacije: </h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Proces aplikacije'])+'</p>', unsafe_allow_html=True)
            st.markdown('<h5>Lista neophodnih dokumenata: </h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Lista neophodnih dokumenata'])+'</p>', unsafe_allow_html=True)

        with tab3:
            st.markdown('<p>'+str(row['Dodatne napomene'])+'</p>', unsafe_allow_html=True)

    #services['Servis'] = services['Tip usluge/prava/benefita']
#lista_usluga = services['Servis'].unique()
#useri =  services['Korisnici'].unique()

#col1, col2 = st.columns(2)
#with col1:
#kategorija = st.selectbox('Odaberite Tip usluge/prava/benefita:',lista_usluga)

#with col2:
#users = st.selectbox('Odaberite kategoriju korisnika:',useri)

#df = services.query('Servis == "'+str(kategorija)+'" & Korisnici == "'+str(users)+'"')
#st.write(df)

#true_html = '<input type="checkbox" checked disabled="true">'
#st.divider()
#for index, row in df.iterrows():
#st.markdown('<p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Servis'])+'</p><p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Korisnici'])+'<p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Godine'])+'</p>', unsafe_allow_html=True)
#st.markdown('<p style="margin:0;display:inline;float:left" class="blog-label">'+str(row['Age'])+'</p>', unsafe_allow_html=True)
#st.markdown('<p style="margin:0;display:inline;float:left" class="blog-label">'+str(row['Users'])+'</p>', unsafe_allow_html=True)
#st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
#st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)
#st.markdown('<p><b>Pravni osnov:</b><br>'+str(row['Pravni osnov'])+'</p>', unsafe_allow_html=True)
#st.divider()
#st.write('Government Agency/Organization')
#st.markdown('<h4>'+str(row['Government Agency/Organization'])+'</h3>', unsafe_allow_html=True)

#col3, col4 = st.columns(2)
#with col3:
#st.write('<p style="font-size:18px;"><b>Ministarstvo/Organizacija</b></p>',
#unsafe_allow_html=True)
#st.write(row['Ministartvo/Organ izacija'])
#st.write(row['Adresa'])
#st.write(row['Telefon'])
#st.write(row['Email'])
#st.link_button("Website", row['Web stranica'])

#m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
#folium.Marker(
#[39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell").add_to(m)

# call to render Folium map in Streamlit
#st_data = st_folium(m, height=250, width=250)

#with col4:
#st.write('<p style="font-size:18px;"><b>Proces aplikacije i potrebni dokumenti</b></p>',
#unsafe_allow_html=True)
#st.write(str(row['Proces aplikacije']))
#st.write('Neophodna lista dokumenata: '+str(row['Lista neophodnih dokumenata']))
#st.write('Vremenski okvir: '+str(row['Vremenski okvir']))
#st.write('Dodatne napomene: '+str(row['Dodatne napomene']))
#st.link_button("Link za informacije o prijavi", str(row['Link za informacije o prijavi']))
#st.divider()