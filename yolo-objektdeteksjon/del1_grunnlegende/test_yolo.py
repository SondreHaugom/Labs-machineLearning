from webbrowser import get
from ultralytics import YOLO
import streamlit as st
from PIL import Image
import csv
from datetime import datetime
import inquirer


def logg_deteksjon(fil, klasse, konfidens, boks):
    with open(fil, mode='a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
             datetime.now().strftime("%Y-%m-%d %H:%M%S"),
             klasse,f"{konfidens:.2f}",
             *[int(v) for v in boks]
        ])




modell = YOLO("best.pt")          # laster ned automatisk første gang



result = modell(
    "yolo-objektdeteksjon/del1_grunnlegende/20260528_133629.jpg",
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





"""
def fileInput():
    st.title("YOLOv8 Object Detection")
    uploaded_file = st.file_uploader("Last opp et bilde", type=["jpg"]).lower()
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Lastet opp bilde", use_column_width=True)
        return uploaded_file.lower() 
    else:
        st.warning("Vennligst last opp et bilde for deteksjon.")
        return None

"""