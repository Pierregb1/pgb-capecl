import pandas as pd
#pip install openyxl
def convcsvliste(fichier_excel):
    
    df = pd.read_excel(fichier_excel)
    
   
    colonnes_dict = {colonne: df[colonne].tolist() for colonne in df.columns}
    
    return colonnes_dict

fichier_excel = 'C:/Users/pierr/Downloads/valeur tp8 q1.xlsx'   #METTRE LES ESPACES POUR LE NOM DU FICHIER (SEULE LIGNE A MODIFIER)
resultats = convcsvliste(fichier_excel)


for colonne, valeurs in resultats.items():
    print(f"Colonne '{colonne}': {valeurs}")



