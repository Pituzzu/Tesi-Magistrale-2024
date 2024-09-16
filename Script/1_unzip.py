import zipfile
import os

# Percorso del file ZIP e della cartella di destinazione
zip_file_path = '/home/pituzzu/Scrivania/Tesi Magistrale/Package Tesi/img_align_celeba.zip'
extract_to_path = '/home/pituzzu/Scrivania/Tesi Magistrale/Dataset'
backup_dataset = '/home/pituzzu/Scrivania/Tesi Magistrale/Backup_Dataset'

# Creazione della cartella di destinazione se non esiste
os.makedirs(extract_to_path, exist_ok=True)

# Estrazione dei file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f'I file sono stati estratti in: {extract_to_path}')
