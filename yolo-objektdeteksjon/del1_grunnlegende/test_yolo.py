from ultralytics import YOLO

modell = YOLO("best.pt")          # laster ned automatisk første gang

result = modell(
    "yolo-objektdeteksjon/del1_grunnlegende/20260528_122934.jpg",
    conf=0.70, # minimun confidence for å beholde deteksjonen
    iou=0.30, # 
    max_det=10, # maks antall deteksjoner per bilde
    agnostic_nms=True, # ikke skille mellom klasser ved NMS
)

result[0].save("Resultat.jpg") # lagrer bildet med deteksjoner i samme mappe som scriptet

for boks in result[0].boxes:
    klasse = result[0].names[int(boks.cls[0])]
    koordinater = boks.xyxy[0].tolist()
    print(f"Klasse: {klasse}, Koordinater: {koordinater}")