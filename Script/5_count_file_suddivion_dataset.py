path_day = "dataset_25_09_24"
percorso_cartella = '/home/pituzzu/Scrivania/Tesi Magistrale/'+path_day+'/4_3_Dataset'

import os

def conta_file_in_cartelle(percorso_base):
    totale_file = 0
    for root, dirs, files in os.walk(percorso_base):
        totale_file += len(files)
    return totale_file

totale = conta_file_in_cartelle(percorso_cartella)
print(f"Il totale dei file è: {totale}")
