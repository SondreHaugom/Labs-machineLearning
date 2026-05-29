from yolo_objektdeteksjon.del2_webkamera.kamera_deteksjon import kamera_deteksjon
import csv
from datetime import datetime
import inquirer


valg_liste = [
    "Start deteksjon",
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
          if userInput == "Start deteksjon":
               print("Starter deteksjon...")
               kamera_deteksjon()
               logg_deteksjon()
          elif userInput == "Avslutt":
                print("Avslutter programmet.")
                break
