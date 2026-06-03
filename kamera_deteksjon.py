import cv2
import time 
from ultralytics import YOLO
from logg_deteksjon import logg_deteksjon


def kamera_deteksjon():
    try:
        modell = YOLO("best.pt")          # laster ned automatisk første gang
        if not modell:
            print("Feil ved innlastning av modellen")
            return
        
        kamera = cv2.VideoCapture(0) # 0 for innebygd kamera, 1 for ekstern
        forrige_tid = time.time()

        while True:
            suksess, frame = kamera.read()
            if not suksess:
                print("Feil ved innlesning av kamera")
                break
            
            resultater = modell(frame, verbose=False)
            annotert = resultater[0].plot()
            fps = 1 / (time.time() - forrige_tid)

           #logg_deteksjon("deteksjoner.csv", "Live Deteksjon", resultater, annotert) # Logg for live deteksjon

            forrige_tid = time.time()
            cv2.putText(annotert, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Deteksjon", annotert)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Avslutter deteksjon")
                break
    except Exception as e:
        print(f"En feil oppsto: {e}")
    finally:
        kamera.release()
        cv2.destroyAllWindows()