from ultralytics import YOLO

model = YOLO("runs/detect/train-2/weights/best.pt")

results = model.predict(
    source="dataset/four clover -leaf/test/images/four116.jpg",
    save=True,
    conf=0.25
)

print("DONE!")