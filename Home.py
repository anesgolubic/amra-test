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


#col1, col2, col3 = st.columns(3)
#with col1:
#    st.image('UNWomen logo.png')
#with col3:
#    st.image('Sweden_logotype_Bosnia.png', width=212)
"""
# Prava i usluge za osobe sa invaliditetom, osobe treće životne dobi i njihove porodice u Kantonu Sarajevo
"""
st.write('Cilj ovog projekta je kroz transparentno informiranje o pravima i uslugama, doprinijeti ekonomskom osnaživanju, prvenstveno korisnica i njegovateljica osoba sa invaliditetom, ali i svih osoba koje imaju navedene potrebe a posebno naših sugrađana i sugrađanki treće životne dobi. Prikaz nudi informacije o pravima i uslugama razvrstane u tri kategorije:')
tab1, tab2, tab3 = st.tabs(["Administrativni postupci", "Diskrecione usluge", "Neinstitucionalizirana prava"])
with tab1:
    st.write('Administrativni postupci - Ova kategorija obuhvata prava i usluge koje su jasno definirane u zakonu i propisima, te su institucionalizirane putem administrativnih postupaka. Procedura za ostvarivanje ovih prava je precizno navedena, uključujući popis potrebnih dokumenata i očekivani ishod za svaku podnositeljicu ili podnositelja zahtjeva.')
with tab2:
    st.write('Diskrecione usluge - Ova kategorija obuhvata usluge koja ovise o odlukama određenih osoba na pozicijama unutar institucija ili su uslovljene varijabilnim faktora kao što je visina planiranog budžet. Procedura može varirati prema mjestu boravka, a u nekim slučajevima nemoguće je identificirati listu potrebnih dokumenata za ostvarivanje prava.')
with tab3:
    st.write('Neinstitucionalizirana prava - Ova kategorija obuhvata prava koja su prepoznata u zakonodavstvu, ali nisu institucionalizirana ili ne postoje formalizirani postupci za njihovo ostvarivanje.')
st.write('Prikaz je je razvijen u decembru 2023. godine, za potrebe UN Women, finansiran od strane ambasade Švedske, te je stavljen na raspolaganje Vladi Kantona Sarajevo. UN Women ne snosi odgovornost za ispravnost informacija na ovom materijalu nakon decembra 2023. godine. Obzirom na ograničenja po pitanju dostupnosti informacija i učestalih izmjena propisa, posebno u pogledu diskrecionih usluga, ova mapa se ne treba smatrati konačnom. ')


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
df['Tip usluge/prava/benefita'] = df['Tip usluge/prava/benefita'].fillna('Ostalo')
df.rename(columns={"Tip usluge/prava/benefita": "Usluga","Životna dob":"Životna_dob"}, inplace=True)


df['Životna_dob2'] = df['Životna_dob'].str.lower()
df['Životna_dob2'] = df['Životna_dob2'].str.split('; ')

df[['Opis','Ministartvo/Organizacija','Adresa','Web stranica','Telefon','Email','Pravni osnov','Proces aplikacije','Lista neophodnih dokumenata','Link za informacije o prijavi','Dodatne napomene','Pravni okvir','Pojašnjenje (Član)']] = df[['Opis','Ministartvo/Organizacija','Adresa','Web stranica','Telefon','Email','Pravni osnov','Proces aplikacije','Lista neophodnih dokumenata','Link za informacije o prijavi','Dodatne napomene','Pravni okvir','Pojašnjenje (Član)']]. fillna('')

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

usluge = list(set(df['Usluga'].unique()))


#Filteri
col1, col2 = st.columns(2)
with col1:
    zivotna_dob = st.selectbox('Odaberite životnu dob:',options=zd,placeholder='Izaberi neku od opcija', index=1)

with col2:
    usluga = st.selectbox('Odaberite tip usluge/prava:',options=usluge,placeholder='Izaberi neku od opcija', index=2)

st.write('usluge')

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

dff1 = dff.query("Kategorija == 'Administrativni postupci'")
i = 0
if len(dff1) > 0:
    st.subheader('Administrativni postupci')
    st.write('Ovdje možete dobiti pregled prava i usluga, za osobe sa invaliditetom, osobe treće životne dobi i njihove porodice u Kantonu Sarajevo. Ovaj pregled je rezultat potrebe identificirane kroz Polaznu studiju o ekonomiji brige i njege u Bosni i Hercegovini iz 2023., naručene od strane UN Women, a finansirane od strane ambasade Švedske.')
    for index,row in dff1.iterrows():
        with st.expander(row['Naziv ']):
            st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
            st.markdown('<p style="margin-top:10px;display:inline;float:left" class="blog-label">'+str(row['Usluga'])+'</p><p style="margin-left:5px;margin-top:10px;display:inline;float:left" class="blog-label">'+str(zivotna_dob)+'</p>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                if len(row['Pravni okvir']) > 0:
                    st.markdown('<h5>Pravni okvir:</h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Pravni okvir'])+'</p>', unsafe_allow_html=True)
            with col2:
                if len(row['Pojašnjenje (Član)']) > 0:
                    st.markdown('<h5>Pojašnjenje (Član):</h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Pojašnjenje (Član)'])+'</p>', unsafe_allow_html=True)

            st.divider()

            tab1, tab2, tab3 = st.tabs(["Ministarstvo/Organizacija", "Proces aplikacije", "Dodatne napomene"])
            with tab1:
                st.markdown('<h5>'+str(row['Ministartvo/Organizacija'])+'</h5>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Adresa'])+'</p>', unsafe_allow_html=True)
                st.markdown('<a href="+'+str(row['Web stranica'])+'">'+str(row['Web stranica'])+'</a>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Telefon'])+'</p>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Email'])+'</p>', unsafe_allow_html=True)

                if row['Lat'] > 0:
                    fig = px.scatter_mapbox(dff1.iloc[[i]], lat="Lat", lon="Lon", zoom=15, height=300, hover_name="Ministartvo/Organizacija",
                                            hover_data={'Lat':False, 'Lon':False, 'Adresa':True})
                    fig.update_layout(mapbox_style="carto-positron")
                    fig.update_traces(marker={'size': 15})
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig, use_container_width=True, config=dict(
                        displayModeBar=False))
                    i += 1
                else:
                    i += 1

            with tab2:
                if len(row['Proces aplikacije']) > 0:
                    st.markdown('<h5>Proces aplikacije: </h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Proces aplikacije'])+'</p>', unsafe_allow_html=True)
                if len(row['Lista neophodnih dokumenata']) > 0:
                    st.markdown('<h5>Lista neophodnih dokumenata: </h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Lista neophodnih dokumenata'])+'</p>', unsafe_allow_html=True)

            with tab3:
                if len(row['Dodatne napomene']) > 0:
                    st.markdown('<p>'+str(row['Dodatne napomene'])+'</p>', unsafe_allow_html=True)

dff2 = dff.query("Kategorija == 'Diskrecione usluge'")
j = 0
if len(dff2) > 0:
    st.subheader('Diskrecione usluge')
    st.write('Ova kategorija obuhvata usluge za osobe s invaliditetom koja ovise o diskrecijskim odlukama određenih osoba i institucija ili faktora. Procedura može varirati, a u nekim slučajevima nisu precizno definirani svi potrebni dokumenti.')
    for index,row in dff2.iterrows():
        with st.expander(row['Naziv ']):
            st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
            st.markdown('<p style="margin-top:10px;display:inline;float:left" class="blog-label">'+str(row['Usluga'])+'</p><p style="margin-left:5px;margin-top:10px;display:inline;float:left" class="blog-label">'+str(zivotna_dob)+'</p>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                if len(row['Pravni okvir']) > 0:
                    st.markdown('<h5>Pravni okvir:</h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Pravni okvir'])+'</p>', unsafe_allow_html=True)
            with col2:
                if len(row['Pojašnjenje (Član)']) > 0:
                    st.markdown('<h5>Pojašnjenje (Član):</h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Pojašnjenje (Član)'])+'</p>', unsafe_allow_html=True)

            st.divider()

            tab1, tab2, tab3 = st.tabs(["Ministarstvo/Organizacija", "Proces aplikacije", "Dodatne napomene"])
            with tab1:
                st.markdown('<h5>'+str(row['Ministartvo/Organizacija'])+'</h5>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Adresa'])+'</p>', unsafe_allow_html=True)
                st.markdown('<a href="+'+str(row['Web stranica'])+'">'+str(row['Web stranica'])+'</a>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Telefon'])+'</p>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Email'])+'</p>', unsafe_allow_html=True)

                if row['Lat'] > 0:
                    fig = px.scatter_mapbox(dff2.iloc[[j]], lat="Lat", lon="Lon", zoom=15, height=300, hover_name="Ministartvo/Organizacija",
                                            hover_data={'Lat':False, 'Lon':False, 'Adresa':True})
                    fig.update_layout(mapbox_style="carto-positron")
                    fig.update_traces(marker={'size': 15})
                    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
                    st.plotly_chart(fig, use_container_width=True, config=dict(
                        displayModeBar=False))
                    j += 1
                else:
                    j += 1

            with tab2:
                if len(row['Proces aplikacije']) > 0:
                    st.markdown('<h5>Proces aplikacije: </h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Proces aplikacije'])+'</p>', unsafe_allow_html=True)
                if len(row['Lista neophodnih dokumenata']) > 0:
                    st.markdown('<h5>Lista neophodnih dokumenata: </h5>', unsafe_allow_html=True)
                    st.markdown('<p>'+str(row['Lista neophodnih dokumenata'])+'</p>', unsafe_allow_html=True)

            with tab3:
                if len(row['Dodatne napomene']) > 0:
                    st.markdown('<p>'+str(row['Dodatne napomene'])+'</p>', unsafe_allow_html=True)

dff3 = dff.query("Kategorija == 'Neinstitucionalizirana prava'")
if len(dff3) > 0:
    st.subheader('Neinstitucionalizirana prava')
    st.write('Ova kategorija obuhvata prava koja su prepoznata u zakonodavstvu, ali nisu institucionalizirana ili ne postoje formalizirani postupci za njihovo ostvarivanje.')
    for index,row in dff3.iterrows():
        with st.expander(row['Naziv ']):
            st.markdown('<h3>'+str(row['Naziv '])+'</h3>', unsafe_allow_html=True)
            st.markdown('<p style="margin-top:10px;display:inline;float:left" class="blog-label">'+str(row['Usluga'])+'</p><p style="margin-left:5px;margin-top:10px;display:inline;float:left" class="blog-label">'+str(zivotna_dob)+'</p>', unsafe_allow_html=True)
            st.markdown('<p>'+str(row['Opis'])+'</p>', unsafe_allow_html=True)

            if len(row['Pravni okvir']) > 0:
                st.markdown('<h5>Pravni okvir:</h5>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Pravni okvir'])+'</p>', unsafe_allow_html=True)
            if len(row['Pojašnjenje (Član)']) > 0:
                st.markdown('<h5>Pojašnjenje (Član):</h5>', unsafe_allow_html=True)
                st.markdown('<p>'+str(row['Pojašnjenje (Član)'])+'</p>', unsafe_allow_html=True)
                st.markdown('<a href="+'+str(row['Web stranica'])+'">'+str(row['Web stranica'])+'</a>', unsafe_allow_html=True)

if ((len(dff1) == 0) and (len(dff2) == 0) and (len(dff3) ==0)):
    st.write('Nema rezultata za odabrane vrijednosti. Izmijenite filtere kako bi dobili rezultate.')