import os

# Specifica il percorso della cartella
cartella = '/home/pituzzu/Scrivania/Tesi Magistrale/Dataset/img_align_celeba'

# Ottieni un elenco di tutti i nomi di file e cartelle nella directory
contenuti = os.listdir(cartella)

# Inizializza un contatore per i file
numero_file = 0

# Itera su tutti i nomi ottenuti
for nome in contenuti:
    # Ottieni il percorso completo
    percorso_completo = os.path.join(cartella, nome)
    
    # Verifica se è un file
    if os.path.isfile(percorso_completo):
        # Incrementa il contatore dei file
        numero_file += 1

# Stampa il numero di file trovati
print(f"Numero di file: {numero_file}")
