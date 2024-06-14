
<details open>
<summary>Install</summary>

Pip install the ultralytics package including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml) in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Downloads](https://static.pepy.tech/badge/ultralytics)](https://pepy.tech/project/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```bash
# Clone the ultralytics repository
git clone https://github.com/Yulin1004/LSMA

# Navigate to the cloned directory
cd lsma

# Install the package in editable mode for development
pip install -e .
```

</details>

<details open>
<summary>Usage</summary>

### Python

Run the train or valid file.
</details>

<details open>
<summary>Result</summary>
<table width="1400px" cellspacing="10">
<tr>
  <th align="center">Model</th>
  <th align="center">Precision</th>
  <th align="center">Recall</th>
  <th align="center">mAP50</th>
  <th align="center">mAP50-95</th>
  <th align="center">weights</th>
</tr>
    <tr>
  <td colspan="6" align="center">coco</td>
</tr>
<tr>
    <tr>
      <td align="center">Yolov8</td>
      <td align="center">0.632</td>
      <td align="center">0.475</td>
      <td align="center">0.521</td>
      <td align="center">0.371</td>
      <td align="center"><a href="https://github.com/yancie-yjr/StreamYOLO/releases/download/0.1.0rc/l_s50_one_x.pth">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(SE)</td>
      <td align="center">0.627</td>
      <td align="center">0.494</td>
      <td align="center">0.533</td>
      <td align="center">0.379</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/co_se.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(CBAM)</td>
      <td align="center">0.637</td>
      <td align="center">0.493</td>
      <td align="center">0.536</td>
      <td align="center">0.378</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/co_cbam.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(ECA)</td>
      <td align="center">0.631</td>
      <td align="center">0.486</td>
      <td align="center">0.531</td>
      <td align="center">0.378</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/co_eca.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(LSMA)</td>
      <td align="center">0.637</td>
      <td align="center">0.499</td>
      <td align="center">0.539</td>
      <td align="center">0.384</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/co_lsma.pt">weight</a></td>
    </tr>
  <tr>
  <tr>
  <td colspan="6" align="center">Pascal VOC</td>
</tr>
<tr>
    <tr>
      <td align="center">Yolov8</td>
      <td align="center">0.784</td>
      <td align="center">0.718</td>
      <td align="center">0.806</td>
      <td align="center">0.594</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/voc_ori.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(SE)</td>
      <td align="center">0.806</td>
      <td align="center">0.715</td>
      <td align="center">0.799</td>
      <td align="center">0.598</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/voc_se.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(CBAM)</td>
      <td align="center">0.812</td>
      <td align="center">0.723</td>
      <td align="center">0.805</td>
      <td align="center">0.599</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/voc_cbam.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(ECA)</td>
      <td align="center">0.801</td>
      <td align="center">0.727</td>
      <td align="center">0.803</td>
      <td align="center">0.601</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/voc_eca.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(LSMA)</td>
      <td align="center">0.815</td>
      <td align="center">0.724</td>
      <td align="center">0.810</td>
      <td align="center">0.607</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/voc_lsma.pt">weight</a></td>
    </tr>
  <tr>
  <td colspan="6" align="center">BDD100K</td>
</tr>
<tr>
    <tr>
      <td align="center">Yolov8</td>
      <td align="center">0.573</td>
      <td align="center">0.427</td>
      <td align="center">0.466</td>
      <td align="center">0.261</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/bdd_ori.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(SE)</td>
      <td align="center">0.675</td>
      <td align="center">0.431</td>
      <td align="center">0.473</td>
      <td align="center">0.265</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/bdd_se.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(CBAM)</td>
      <td align="center">0.691</td>
      <td align="center">0.426</td>
      <td align="center">0.474</td>
      <td align="center">0.266</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/bdd_cbam.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(ECA)</td>
      <td align="center">0.588</td>
      <td align="center">0.431</td>
      <td align="center">0.477</td>
      <td align="center">0.268</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/bdd_eca.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(LSMA)</td>
      <td align="center">0.594</td>
      <td align="center">0.434</td>
      <td align="center">0.479</td>
      <td align="center">0.269</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/bdd_lsma.pt">weight</a></td>
    </tr>
  </tr>
<tr>
  <td colspan="6" align="center">Udacity</td>
</tr>
<tr>
    <tr>
      <td align="center">Yolov8</td>
      <td align="center">0.829</td>
      <td align="center">0.703</td>
      <td align="center">0.776</td>
      <td align="center">0.484</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/uda_ori.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(SE)</td>
      <td align="center">0.826</td>
      <td align="center">0.704</td>
      <td align="center">0.784</td>
      <td align="center">0.488</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/uda_se.pt">weight</a></td>
    </tr>
    <tr>
      <td align="center">Yolov8_Att(CBAM)</td>
      <td align="center">0.828</td>
      <td align="center">0.703</td>
      <td align="center">0.784</td>
      <td align="center">0.489</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/uda_cbam.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(ECA)</td>
      <td align="center">0.834</td>
      <td align="center">0.706</td>
      <td align="center">0.780</td>
      <td align="center">0.483</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/uda_eca.pt">weight</a></td>
    </tr>
      <tr>
      <td align="center">Yolov8_Att(LSMA)</td>
      <td align="center">0.839</td>
      <td align="center">0.709</td>
      <td align="center">0.788</td>
      <td align="center">0.494</td>
      <td align="center"><a href="https://github.com/Yulin1004/LSMA/releases/download/V1.0/uda_lsma.pt">weight</a></td>
    </tr>
</table>

</details>
