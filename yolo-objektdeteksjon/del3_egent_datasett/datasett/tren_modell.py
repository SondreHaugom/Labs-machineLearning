from ultralytics import YOLO
from pathlib import Path

model = YOLO("yolo11n.pt")

model.train(
    data=Path(__file__).parent / "dataset.yaml",
    epochs=50,
    imgsz=640,
)
