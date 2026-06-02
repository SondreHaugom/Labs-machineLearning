from kamera_deteksjon import kamera_deteksjon
import csv
from datetime import datetime
import inquirer
from ultralytics import YOLO

valg_liste = [
    "Start live deteksjon",
    "Legg til bilde for deteksjon",
    "Avslutt"
]


# Funksjon for å logge deteksjoner til en CSV-fil
def bilde_deteksjon():
    model = YOLO("best.pt")

    result = model(
        "yolo-objektdeteksjon/del1_grunnlegende/20260528_133629.jpg",
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






# Funksjon for å logge deteksjoner til en CSV-fil
def logg_deteksjon(fil, klasse, konfidens, boks):
    with open(fil, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
             datetime.now().strftime("%Y-%m-%d %H:%M%S"),
             klasse,f"{konfidens:.2f}",
             *[int(v) for v in boks]
        ])




if __name__ == "__main__":
     while True:
        userInput = inquirer.list_input("Velg et alternativ:", choices=valg_liste)
        if userInput == "Start live deteksjon":
            print("Starter live deteksjon...")
            logg_deteksjon("deteksjoner.csv", "Live Deteksjon", 0.0, [0, 0, 0, 0]) # Logg for live deteksjon
            kamera_deteksjon()
          
        elif userInput == "Legg til bilde for deteksjon":
            print("Legger til bilde for deteksjon...")
            bilde_deteksjon()


        elif userInput == "Avslutt":
            print("Avslutter programmet.")
            break