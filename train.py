from ultralytics import YOLO

model = YOLO("best.pt")

results = model.predict(
    source="data.yaml",
    epochs = 50,
    imgsz = 640
)