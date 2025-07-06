# 🚘 YOLOv5-Based Number Plate Recognition System

A real-time number plate recognition system using YOLOv5 object detection. This project detects and extracts vehicle license plates from images and videos with high accuracy, useful for smart parking systems, traffic monitoring, and access control.


## 📌 Key Features

- 🚗 Detects vehicle number plates using YOLOv5
- 🧠 Trained on custom-labeled dataset
- 🎯 Achieves 95%+ detection accuracy
- 🎥 Supports real-time video stream input
- 🔍 Extracts plate region for further OCR processing (optional)


## 🛠️ Tech Stack

- 🐍 Python
- 🧠 YOLOv5 (Ultralytics)
- 📦 PyTorch
- 🖼️ OpenCV
- 🗃️ Custom annotated dataset (Roboflow or manual)


## 📁 Project Structure

```

yolov5-number-plate-detection/
├── data/                  # Images + labels (YOLO format)
├── runs/                  # Saved YOLOv5 runs (optional)
├── models/                # Pretrained/best.pt weights
├── detect.py              # YOLOv5 detection script
├── train.py               # Script to train custom model
├── requirements.txt
└── README.md

````


## 🚀 How to Use

### 1️⃣ Clone YOLOv5 + This Repo
```bash
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
````

### 2️⃣ Add Custom Files

* Copy your `data/`, `models/`, and `detect.py` into the YOLOv5 folder

### 3️⃣ Run Detection

```bash
python detect.py --weights models/best.pt --source data/test_image.jpg
```


## 🧪 Results & Accuracy

| Metric        | Value |
| ------------- | ----- |
| Precision     | 0.96  |
| Recall        | 0.94  |
| mAP\@0.5      | 95.3% |
| Inference FPS | \~25  |

> Model trained on 500+ annotated images of vehicles using YOLOv5s.


## 🧠 Training (Optional)

1. Annotate using [Roboflow](https://roboflow.com/) or labelImg
2. Export in YOLOv5 format
3. Train with:

```bash
python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt --cache
```


## 📸 Sample Output

```
📷 _Sample detection screenshots and demo video will be added soon._
```

## 👨‍💻 Author

Muhammad Mubashir
📧 [mubashiryaseen@hotmail.com](mailto:mubashiryaseen@hotmail.com)
🔗 [GitHub](https://github.com/mubashir-yaseen)


## 📄 License

MIT License

```
