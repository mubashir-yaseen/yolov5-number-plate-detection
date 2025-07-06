import torch
from pathlib import Path
from yolov5.detect import run

# Entry point for custom detection
if __name__ == "__main__":
    run(
        weights='models/best.pt',
        source='data/test_image.jpg',
        conf_thres=0.25,
        iou_thres=0.45,
        max_det=1000,
        device='',
        save_txt=True,
        save_conf=True,
        save_crop=True,
        project='runs/detect',
        name='number_plate',
        exist_ok=True
    )
