import os
import shutil

numero_img_per_persona = 20
path_day = "dataset_25_09_24"

def elimina_cartelle_con_meno_di_10_immagini(percorso_base):
    for root, dirs, files in os.walk(percorso_base):
        for nome_cartella in dirs:
            percorso_cartella = os.path.join(root, nome_cartella)
            conteggio_immagini = 0
            
            # Conta le immagini nella cartella
            for file in os.listdir(percorso_cartella):
                if file.endswith(('.jpg', '.jpeg', '.png')):
                    conteggio_immagini += 1
            
            # Se la cartella ha meno di 10 immagini, viene eliminata
            if conteggio_immagini < numero_img_per_persona:
                shutil.rmtree(percorso_cartella)
                print(f"Cartella '{percorso_cartella}' eliminata, conteneva {conteggio_immagini} immagini.")

percorso_base = "/home/pituzzu/Scrivania/Tesi Magistrale/"+path_day+"/4_3_Dataset"
elimina_cartelle_con_meno_di_10_immagini(percorso_base)
