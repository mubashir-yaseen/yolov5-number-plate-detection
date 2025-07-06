import os
from yolov5.train import run

# Entry point for training
if __name__ == "__main__":
    run(
        img=640,
        batch=16,
        epochs=50,
        data='data.yaml',
        weights='yolov5s.pt',
        cache=True
    )
