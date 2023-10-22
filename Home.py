import streamlit as st
st.set_page_config(
    page_title="Amra test",
    #page_icon="🧊",
    layout="wide",
)

import pandas as pd
from streamlit_modal import Modal
import streamlit.components.v1 as components
import folium
from streamlit_folium import st_folium, folium_static
#from datetime import date, timedelta
#import numpy as np

# LINK TO THE CSS FILE
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

"""
# Amra test
## Neki podnaslov
"""

df = pd.read_excel('amra_new_file.xlsx')
st.write(df)

df['Tip usluge/prava/benefita'] = df['Tip usluge/prava/benefita'].fillna('Nepoznato')
df.rename(columns={"Tip usluge/prava/benefita": "Usluga","Životna dob":"Životna_dob"}, inplace=True)

zd = df['Životna_dob'].unique()
usluge = df['Usluga'].unique()

#Filteri
col1, col2 = st.columns(2)
with col1:
    zivotna_dob = st.selectbox('Odaberite životnu dob:',zd)

with col2:
    usluga = st.selectbox('Odaberite Tip usluge/prava/benefita:',usluge)

#Filtriranje dataframe-a
dff = df.query("Životna_dob == '"+str(zivotna_dob)+"' & Usluga == '"+str(usluga)+"'")

for index,row in dff.iterrows():
    with st.expander(row['Naziv ']):
        st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
        st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<h5>Pravo:</h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Pravo'])+'</p>', unsafe_allow_html=True)
        with col2:
            st.markdown('<h5>Pravni osnov:</h5>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Pravni osnov'])+'</p>', unsafe_allow_html=True)


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