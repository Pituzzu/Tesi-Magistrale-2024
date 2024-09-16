import os
import shutil

# Percorso alla cartella principale e al file di identità
base_path = "/home/pituzzu/Scrivania/Tesi Magistrale/Backup_Dataset"  # Sostituisci con il percorso della tua cartella Dataset
images_dir = os.path.join(base_path, "img_align_celeba")
identities_file = os.path.join(base_path, "/home/pituzzu/Scrivania/Tesi Magistrale/Package Tesi/identity_CelebA.txt")

# Directory per memorizzare le immagini organizzate per persona
organized_dir = os.path.join(base_path, "4_3_Dataset")

# Crea la directory organizzata se non esiste
os.makedirs(organized_dir, exist_ok=True)

# Dizionario per mappare gli ID delle persone alle immagini corrispondenti
person_to_images = {}

# Leggi il file di identità
with open(identities_file, 'r') as file:
    for line in file:
        image_file, person_id = line.strip().split()
        person_id = int(person_id)
        if person_id not in person_to_images:
            person_to_images[person_id] = []
        person_to_images[person_id].append(image_file)

# Creazione delle cartelle per ogni persona e spostamento delle immagini
for person_id, images in person_to_images.items():
    person_dir = os.path.join(organized_dir, str(person_id))
    os.makedirs(person_dir, exist_ok=True)
    for image_file in images:
        src = os.path.join(images_dir, image_file)
        dst = os.path.join(person_dir, image_file)
        if os.path.exists(src):
            shutil.move(src, dst)
