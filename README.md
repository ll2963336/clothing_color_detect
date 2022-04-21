# 顏色識別

## 步驟：

1. 確保電腦連上`cam`
2.

```
> 逐步進行以下步驟：

pip install -r requirement.txt

python MovenetOpenvino.py
```

## 其他事項：

1. 若出現`A problem occurred in initializing MCI`的 error，請參考該網址：
   https://blog.csdn.net/weixin_50836014/article/details/122135430

## 幫助

```
> python3 MovenetOpenvino.py -h
usage: MovenetOpenvino.py [-h] [-i INPUT] [-p {16,32}]
                          [-m {lightning,thunder}] [--xml XML] [-d DEVICE]
                          [-s SCORE_THRESHOLD] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to video or image file to use as input
                        (default=0)
  -p {16,32}, --precision {16,32}
                        Precision (default=32
  -m {lightning,thunder}, --model {lightning,thunder}
                        Model to use (default=thunder
  --xml XML             Path to an .xml file for model
  -d DEVICE, --device DEVICE
                        Target device to run the model (default=CPU)
  -s SCORE_THRESHOLD, --score_threshold SCORE_THRESHOLD
                        Confidence score to determine whether a keypoint
                        prediction is reliable (default=0.200000)
  -o OUTPUT, --output OUTPUT
                        Path to output video file
  -wi WIDTH, --width WIDTH
                        window移動的x軸距離，默認為0
  -hi HEIGHT, --height HEIGHT
                        window移動的y軸距離，默認為0
  -wd WINDOW, --window WINDOW
                        選擇想要移動的window，默認為0
```
