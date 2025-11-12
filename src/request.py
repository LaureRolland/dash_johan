#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 12:29:39 2025

@author: lrolland
"""

"""
palette de couleurs
#EEE2DF
#EED7C5
#C89F9C
#CA7C5C
#B36A5E
#392E2C
"""

import pandas as pd
import requests
from io import BytesIO


def read_google_sheet():

    # ID de ton fichier Google Sheets
    sheet_id = "1TFN1Ah_D_3C8hpMhKoBdadWOzEmD02WHeozOq4SElUs"
    
    sheet_names = ["Compétitions", "Données", "Records", "Statistiques"]
    
    # URL pour télécharger le Google Sheet entier en Excel
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=xlsx"
    
    # Télécharger le fichier en mémoire (pas besoin de le sauvegarder sur le disque)
    response = requests.get(url)
    excel_data = BytesIO(response.content)
    
    # Lecture de toutes les feuilles à la fois → dictionnaire {nom_onglet: DataFrame}
    sheets_dict = pd.read_excel(excel_data, sheet_name=None)
    
    #reprendre le header onglet compétition
    df_compet = sheets_dict['Compétitions']
    header_row = 2  # la ligne que tu veux comme index
    df_compet.columns = df_compet.iloc[header_row]  # Définir les colonnes
    # Supprimer toutes les lignes avant (y compris celle utilisée comme header)
    df_compet = df_compet.iloc[header_row + 1:].reset_index(drop=True)
    sheets_dict['Compétitions'] = df_compet
 
    return sheets_dict 

# def affichage(df):
    

# def get_data_competitions(df):

def get_data_record(sheets_dict):
    df_records = sheets_dict['Records']
    header_row = 0  # la ligne que tu veux comme index
    df_records.columns = df_records.iloc[header_row]  # Définir les colonnes
    # Supprimer toutes les lignes avant (y compris celle utilisée comme header)
    df_records = df_records.iloc[header_row + 1:].reset_index(drop=True) 
    df_piste = df_records.iloc[:, :5]
    
    df_hors_stade = df_records.iloc[:2, 6:]
    
    return df_piste, df_hors_stade




