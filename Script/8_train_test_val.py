import os
import shutil
import random


path_day = "dataset_25_09_24"

def suddividi_dataset(percorso_base, destinazione, perc_train=0.8, perc_test=0.1, perc_val=0.1):
    # Crea le cartelle di destinazione
    train_dir = os.path.join(destinazione, 'train')
    test_dir = os.path.join(destinazione, 'test')
    val_dir = os.path.join(destinazione, 'val')
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    
    # Lista di tutte le sottocartelle
    sottocartelle = [os.path.join(percorso_base, d) for d in os.listdir(percorso_base) if os.path.isdir(os.path.join(percorso_base, d))]

    for cartella in sottocartelle:
        immagini = [f for f in os.listdir(cartella) if f.endswith(('.jpg', '.jpeg', '.png'))]
        random.shuffle(immagini)  # Mischia le immagini per una distribuzione casuale

        # Calcola il numero di immagini per ogni insieme
        num_immagini = len(immagini)
        train_count = int(num_immagini * perc_train)
        test_count = int(num_immagini * perc_test)
        val_count = num_immagini - train_count - test_count

        # Creazione delle sottocartelle per ogni cartella nel train, test e val
        nome_cartella = os.path.basename(cartella)
        cartella_train = os.path.join(train_dir, nome_cartella)
        cartella_test = os.path.join(test_dir, nome_cartella)
        cartella_val = os.path.join(val_dir, nome_cartella)

        os.makedirs(cartella_train, exist_ok=True)
        os.makedirs(cartella_test, exist_ok=True)
        os.makedirs(cartella_val, exist_ok=True)

        # Copia delle immagini nei rispettivi insiemi
        for i, immagine in enumerate(immagini):
            src = os.path.join(cartella, immagine)
            if i < train_count:
                dst = os.path.join(cartella_train, immagine)
            elif i < train_count + test_count:
                dst = os.path.join(cartella_test, immagine)
            else:
                dst = os.path.join(cartella_val, immagine)
            shutil.copy2(src, dst)

    print("Distribuzione completata.")

# Percorsi principali
percorso_base = "/home/pituzzu/Scrivania/Tesi Magistrale/"+path_day+"/4_3_Dataset"
destinazione = "/home/pituzzu/Scrivania/Tesi Magistrale/"+path_day+"/Dataset_train_test_val"

# Esegui la suddivisione
suddividi_dataset(percorso_base, destinazione)
