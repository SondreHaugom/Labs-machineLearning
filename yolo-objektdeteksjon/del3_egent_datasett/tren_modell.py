from ultralytics import YOLO
from pathlib import Path

base_dir = Path(__file__).resolve().parent
workspace_dir = base_dir.parents[1]

model = YOLO(workspace_dir / "yolo11n.pt")

model.train(
    data=base_dir / "data.yaml",
    epochs=30,
    imgsz=440,
    batch=8,
    project=str(base_dir / "tren_modell"),
    name="yolo11n_egent_datasett",
)
result = model.val()
print(result)
