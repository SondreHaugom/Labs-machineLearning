from ultralytics import YOLO

modell = YOLO("best.pt")          # laster ned automatisk første gang
resultater = modell("yolo-objektdeteksjon/del1_grunnlegende/20260528_122934.jpg")
resultater[0].save("resultat.jpg")   # lagrer bilde med bounding boxes

for boks in resultater[0].boxes: # kjører løkke for hver boks i det første resultatet
    klasse = resultater[0].names[int(boks.cls)] 
    konfidens = boks.conf[0.70].item()  # konverterer tensor til float
    iou = boks.iou[0.30].item()  # konverterer tensor til float
    koordinater = boks.xyxy[0].tolist()
    print(f"{klasse}: {konfidens:.2f} – {koordinater}")
 

 