from yolo_objektdeteksjon.del2_webkamera.kamera_deteksjon import kamera_deteksjon
import csv
from datetime import datetime
import inquirer


valg_liste = [
    "Start live deteksjon",
    "Legg til bilde for deteksjon",
    "Avslutt"
]


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
            kamera_deteksjon()
          
        
        elif userInput == "Legg til bilde for deteksjon":
            print("Funksjonalitet for bildeopplasting er under utvikling.")


        elif userInput == "Avslutt":
            print("Avslutter programmet.")
            break