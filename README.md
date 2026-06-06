# Four-Leaf Clover Detector 🍀

A custom YOLOv8 object detection model trained to identify four-leaf clovers in images.

## Features
- Custom-trained YOLOv8 model
- Detects four-leaf clovers
- Built using Roboflow and Ultralytics

## Project Structure

- train.py - model training
- test.py - model inference
- data.yaml - dataset configuration
- runs/train2/weights/best.pt - trained model

## Training

```bash
python train.py


---

## Step 5: Commit

In VS Code Source Control:

Stage:

✅ `train.py`  
✅ `test.py`  
✅ `data.yaml`  
✅ `README.md`  
✅ `.gitignore`  
✅ `weights/best.pt`

You can leave unstaged:

❌ `runs/...`  
❌ `.cache` files  
❌ training graphs and prediction images

---

## One More Recommendation

Before pushing to GitHub, add a few lines to your README about:

- Number of images used (around 28)
- Epochs (50)
- Image size (640)
- Future improvements (collecting more data)

That shows anyone viewing the repository that you understand the machine learning workflow, not just the code. 🍀🚀