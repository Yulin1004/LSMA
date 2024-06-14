from ultralytics import YOLO
import sys

def main():
    model = (YOLO(r"E:\code\yolov8_result\VOC\lsma\weights\best.pt"))
    validation_results = model.val(data=r'E:/code/lsma/ultralytics/cfg/datasets/VOC.yaml',
                               imgsz=640,
                               batch=64,
                               iou=0.7,
                               conf=0.001,
                               plots=True,
                               save_hybrid=False,
                               save_json=True,
                               split='val',
                               device="0")

if __name__=='__main__':
    sys.exit(main())