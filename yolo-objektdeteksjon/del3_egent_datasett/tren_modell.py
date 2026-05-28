from ultralytics import YOLO
from pathlib import Path

file_path = Path.cwd() / "yolo-objektdeteksjon/del3_egent_datasett" / "data.yaml"

model = YOLO(file_path.parent / "yolo11n.pt")


model.train(
    data=file_path,
    epochs=30,
    imgsz=448,
    batch=8,
    project=str(file_path.parent / "tren_modell"),
    name="yolo11n_egent_datasett",
)
result = model.val()
print(result)

