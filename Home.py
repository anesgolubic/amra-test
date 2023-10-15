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

services = pd.read_excel('mapiranje_usluga.xlsx',sheet_name='Mapiranje usluga')
st.write(services)
services['Servis'] = services['Tip usluge/prava/benefita']
lista_usluga = services['Servis'].unique()
useri =  services['Korisnici'].unique()

col1, col2 = st.columns(2)
with col1:
    kategorija = st.selectbox('Odaberite Tip usluge/prava/benefita:',lista_usluga)

with col2:
    users = st.selectbox('Odaberite kategoriju korisnika:',useri)

df = services.query('Servis == "'+str(kategorija)+'" & Korisnici == "'+str(users)+'"')
#st.write(df)

true_html = '<input type="checkbox" checked disabled="true">'

for index, row in df.iterrows():
    st.markdown('<p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Servis'])+'</p><p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Korisnici'])+'<p style="margin:5px;display:inline;float:left" class="blog-label">'+str(row['Godine'])+'</p>', unsafe_allow_html=True)
    #st.markdown('<p style="margin:0;display:inline;float:left" class="blog-label">'+str(row['Age'])+'</p>', unsafe_allow_html=True)
    #st.markdown('<p style="margin:0;display:inline;float:left" class="blog-label">'+str(row['Users'])+'</p>', unsafe_allow_html=True)
    st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
    st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)
    st.markdown('<p><b>Pravni osnov:</b><br>'+str(row['Pravni osnov'])+'</p>', unsafe_allow_html=True)
    #st.divider()
    #st.write('Government Agency/Organization')
    #st.markdown('<h4>'+str(row['Government Agency/Organization'])+'</h3>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        html_string = '''
                <h3>'''+row['Ministartvo/Organ izacija']+'''</h3>
                <p>'''+row['Adresa']+'''</p>
                <p>'''+row['Telefon']+'''</p>
                <p>'''+row['Email']+'''</p>
                '''
        components.html(html_string)
        st.link_button("Website", row['Web stranica'])

        m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
        folium.Marker(
            [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
        ).add_to(m)

        # call to render Folium map in Streamlit
        st_data = st_folium(m, height=350, width=350)

    with col4:
        st.components.v1.html(html_string, width=None, height=None, scrolling=False)
        st.write('Proces aplikacije i potrebni dokumenti')
        st.write(str(row['Proces aplikacije']))
        st.write(str(row['Lista neophodnih dokumenata']))
        st.write(str(row['Vremenski okvir']))
        st.write(str(row['Dodatne napomene']))
        st.link_button("Link za informacije o prijavi", str(row['Link za informacije o prijavi']))

    #st.divider()