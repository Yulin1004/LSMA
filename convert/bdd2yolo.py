import re
import os
import json
from tqdm import tqdm


def search_file(data_dir, pattern=r'\.jpg$'):
    root_dir = os.path.abspath(data_dir)
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            if re.search(pattern, f, re.I):
                abs_path = os.path.join(root, f)
                # print('new file %s' % absfn)
                yield abs_path


class Bdd2yolov5:
    def __init__(self):
        self.bdd100k_width = 1280
        self.bdd100k_height = 720
        self.select_categorys = ["bike", "bus", "car", "motor", "person", "rider", "traffic light","traffic sign","train","truck"]  # 自己需要的类别
        self.cat2id = {
            'bike': 0,
            'bus': 1,
            'car': 2,
            'motor': 3,
            'person': 4,
            'rider': 5,
            'traffic light': 6,
            'traffic sign': 7,
            'train': 8,
            'truck': 9
        }

    @property
    def all_categorys(self):
        return ["person", "rider", "car", "bus", "truck", "bike",  # 人 骑手 车 公交车 货车 自行车
                "motor", "traffic light", "traffic sign", "train"]  # 摩托 交通信号灯 交通标志 火车

    def _filter_by_attr(self, attr=None):
        if attr is None:
            return False
        # 过滤掉晚上的图片
        # if attr['timeofday'] == 'night':
        #     return True
        # return False

    def _filter_by_box(self, w, h):
        # size ratio
        # 过滤到过于小的小目标
        # threshold = 0.001
        # if float(w * h) / (self.bdd100k_width * self.bdd100k_height) < threshold:
        #     return True
        return False

    def bdd2yolov5(self, path):
        lines = ""
        with open(path) as fp:
            j = json.load(fp)
            if self._filter_by_attr(j['attributes']):
                return
            for fr in j["frames"]:
                dw = 1.0 / self.bdd100k_width
                dh = 1.0 / self.bdd100k_height
                for obj in fr["objects"]:
                    if obj["category"] in self.select_categorys:
                        idx = self.cat2id[obj["category"]]
                        cx = (obj["box2d"]["x1"] + obj["box2d"]["x2"]) / 2.0
                        cy = (obj["box2d"]["y1"] + obj["box2d"]["y2"]) / 2.0
                        w = obj["box2d"]["x2"] - obj["box2d"]["x1"]
                        h = obj["box2d"]["y2"] - obj["box2d"]["y1"]
                        if w <= 0 or h <= 0:
                            continue
                        if self._filter_by_box(w, h):
                            continue
                        # 根据图片尺寸进行归一化
                        cx, cy, w, h = cx * dw, cy * dh, w * dw, h * dh
                        line = f"{idx} {cx:.6f} {cy:.6f} {w:.6f} {h:.6f}\n"
                        lines += line
                if len(lines) != 0:
                    # 转换后的以*.txt结尾的标注文件我就直接和*.json放一具目录了
                    yolo_txt = path.replace(".json", ".txt")
                    with open(yolo_txt, 'w') as fp2:
                        fp2.writelines(lines)
                # print("%s has been dealt!" % path)


if __name__ == "__main__":
    bdd_label_dir = r"E:\Datasets\bdd100k\labels\100k\val"
    cvt = Bdd2yolov5()
    for path in tqdm(search_file(bdd_label_dir, r"\.json$")):
        cvt.bdd2yolov5(path)