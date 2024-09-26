import zipfile
import os

# Percorso del file ZIP e della cartella di destinazione
zip_file_path = '/home/pituzzu/Scrivania/Tesi Magistrale/Package Tesi/img_align_celeba.zip'
dataset = '/home/pituzzu/Scrivania/Tesi Magistrale/dataset_25_09_24'

# Creazione della cartella di destinazione se non esiste
os.makedirs(dataset, exist_ok=True)

# Estrazione dei file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(dataset)

print(f'I file sono stati estratti in: {dataset}')
