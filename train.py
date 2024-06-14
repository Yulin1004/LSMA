from ultralytics import YOLO
import sys

def main():
    # train
    model = (YOLO(r"path to yaml"))
    # if coco
    # model.load("path to coco pretrain")
    model.train(**{'cfg':'./ultralytics/cfg/default.yaml'})

if __name__=='__main__':
    sys.exit(main())
