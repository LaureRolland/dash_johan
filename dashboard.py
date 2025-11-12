#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 12:29:20 2025

@author: lrolland
"""

import streamlit as st
import src.request as req

st.set_page_config(layout='wide', page_title = 'dash du king', page_icon="🏃‍♂️")
st.markdown("<h1 style='text-align: center; color: #CA7C5C;'>🏃‍♂️ Les exploits du king</h1>", unsafe_allow_html=True)



#site bar
# CSS personnalisé
st.markdown("""
    <style>
        /* Couleur de fond de la sidebar */
        [data-testid="stSidebar"] {
            background-color: #EEE2DF;
        }

        /* Couleur du texte dans la sidebar */
        [data-testid="stSidebar"] * {
            color: #392E2C;
        }
        
        /* Conteneur du selectbox */
        div[data-baseweb="select"] > div {
            background-color: #EEE2DF;   /* couleur de fond du champ fermé */
            color: #392E2C;              /* couleur du texte */
            border-radius: 8px;          /* coins arrondis */
        }
    
        /* Couleur des options dans la liste déroulante */
        div[data-baseweb="popover"] ul {
            background-color: #EEE2DF!important;  /* fond de la liste */
            color: #392E2C !important;              /* texte blanc */
        }
    
        /* Option survolée */
        div[data-baseweb="popover"] li:hover {
            background-color: #B36A5E !important;   /* couleur de survol */
            color: #EEE2DF !important;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Menu")
option = st.sidebar.selectbox('', ['','Compétitions', "Records", 'Stats'])

@st.cache_data
def lire_fichier():
    sheets_dict = req.read_google_sheet()
    return sheets_dict

sheets_dict =  lire_fichier()  

if option == 'Records':
    st.header("Records du king 🥇")
    df_piste, df_hors_piste = req.get_data_record(sheets_dict)
    
    

