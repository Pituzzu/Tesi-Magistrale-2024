import os
from ultralytics import YOLO
from PIL import Image

# Carica il modello YOLOv8n addestrato per il riconoscimento dei volti
modello = YOLO("/home/pituzzu/Scrivania/Tesi Magistrale/Package Tesi/yolov8n-face.pt")

def ritaglia_immagini(percorso_cartella):
    for root, dirs, files in os.walk(percorso_cartella):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                percorso_immagine = os.path.join(root, file)
                immagine = Image.open(percorso_immagine)
                risultati = modello(percorso_immagine)

                # Loop attraverso i risultati del modello
                for risultato in risultati:
                    for detection in risultato.boxes:
                        # Estrae le coordinate del bounding box
                        x1, y1, x2, y2 = map(int, detection.xyxy[0])
                        immagine_croppata = immagine.crop((x1, y1, x2, y2))
                        
                        # Sovrascrive l'immagine originale con quella ritagliata
                        immagine_croppata.save(percorso_immagine)
                        break  # Interrompe il loop dopo il primo ritaglio
                    break  # Interrompe il loop se almeno un volto è stato ritagliato

percorso_cartella = "/home/pituzzu/Scrivania/Tesi Magistrale/Backup_Dataset/4_3_Dataset"
ritaglia_immagini(percorso_cartella)
