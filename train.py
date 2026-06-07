from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset 2\Clover.v1i.yolov8/data.yaml",
    epochs = 50,
    imgsz = 640
)