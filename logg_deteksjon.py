import csv
from datetime import datetime


# Funksjon for å logge deteksjoner til en CSV-fil
def logg_deteksjon(fil, klasse, konfidens, boks):
    with open(fil, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
             datetime.now().strftime("%Y-%m-%d %H:%M%S"),
             klasse,f"{konfidens:.2f}",
             *[int(v) for v in boks]
        ])