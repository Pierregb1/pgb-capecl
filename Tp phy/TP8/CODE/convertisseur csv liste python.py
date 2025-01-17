import csv

def convscvliste(fichier_csv):
    liste = []
    with open(fichier_csv, mode='r', newline='', encoding='utf-8') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            liste.append(ligne)
    return liste

# Exemple d'utilisation :
# fichier_csv = 'chemin/vers/votre/fichier.csv'
# resultats = lire_csv_vers_liste(fichier_csv)
# print(resultats)
