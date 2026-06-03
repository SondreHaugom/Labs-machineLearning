from ultralytics import YOLO
import csv
from datetime import datetime
import tkinter as tk
from tkinter import filedialog


def logg_deteksjon(fil, klasse, konfidens, boks):
    with open(fil, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
             datetime.now().strftime("%Y-%m-%d %H:%M%S"),
             klasse,f"{konfidens:.2f}",
             *[int(v) for v in boks]
        ])


def fileInput():
    root = tk.Tk() # Oppretter et skjult Tkinter-vindu
    root.withdraw() # Skjul hovedvinduet

    file_path = filedialog.askopenfilename(
        title="Velg et bilde for deteksjon",
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )

    if file_path:
        print(f"Valgt fil: {file_path}")
        return file_path
    else:
        print("Ingen fil valgt.")
        return None



modell = YOLO("best.pt")          # laster ned automatisk første gang



result = modell(
    fileInput(),
    conf=0.40, # minimun confidence for å beholde deteksjonen
    iou=0.20, # 
    max_det=10, # maks antall deteksjoner per bilde
    agnostic_nms=True, # ikke skille mellom klasser ved NMS
)

result[0].save("Resultat.jpg") # lagrer bildet med deteksjoner i samme mappe som scriptet

# kjører gjennom en løkke for å skrive ut klasse og koordinater for hver deteksjon
for boks in result[0].boxes:
    klasse = result[0].names[int(boks.cls[0])]
    koordinater = boks.xyxy[0].tolist()
    logg_deteksjon("deteksjoner.csv", klasse, boks.conf[0], koordinater)
    print(f"Klasse: {klasse}, Koordinater: {koordinater}")






