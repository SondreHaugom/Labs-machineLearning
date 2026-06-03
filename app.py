from kamera_deteksjon import kamera_deteksjon
from logg_deteksjon import logg_deteksjon
import inquirer
from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog

valg_liste = [
    "Start live deteksjon",
    "Legg til bilde for deteksjon",
    "Avslutt"
]


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



# Funksjon for å logge deteksjoner til en CSV-fil
def bilde_deteksjon():
    model = YOLO("best.pt")

    result = model(
        fileInput(),
        conf=0.40, # minimun confidence for å beholde deteksjonen
        iou=0.20, # 
        max_det=10, # maks antall deteksjoner per bilde
        agnostic_nms=True, # ikke skille mellom klasser ved NMS
    )

    result[0].save("Resultat.jpg") # lagrer bildet med deteksjoner i samme mappe som scriptet

    for boks in result[0].boxes:
        klasse = result[0].names[int(boks.cls[0])]
        koordinater = boks.xyxy[0].tolist()
        logg_deteksjon("deteksjoner.csv", klasse, boks.conf[0], koordinater)
        print(f"Klasse: {klasse}, Koordinater: {koordinater}")



if __name__ == "__main__":
     while True:
        userInput = inquirer.list_input("Velg et alternativ:", choices=valg_liste)
        if userInput == "Start live deteksjon":
            print("Starter live deteksjon...")
            kamera_deteksjon()
          
        elif userInput == "Legg til bilde for deteksjon":
            print("Legger til bilde for deteksjon...")
            bilde_deteksjon()


        elif userInput == "Avslutt":
            print("Avslutter programmet.")
            break