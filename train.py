from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset/four clover -leaf/data.yaml",
    epochs = 50,
    imgsz = 640
)