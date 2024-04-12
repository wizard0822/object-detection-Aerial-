# Object Detection on Aerial Imaging Dataset

<p align="center">Note: If you're interested in using it, feel free to ⭐️ the repo so we know!</p>

## Dataset
Satellite Imagery Multi-vehicles Dataset (SIMD). It comprises 5,000 images of resolution 1024 x 768 and collectively contains 45,303 objects in 15 different classes of vehicles including cars, trucks, buses, long vehicles, various types of aircrafts and boats. The source images are taken from public satellite imagery available in Google Earth and contain images of multiple locations from seven countries.

## Data Annotations
With each image, the annotation is available as text file. The annotation format can be described as (c, xi, yi, w, h), where c is the object class starting from 0, (xi, yi) are the center of object and (w, h) are width and height respectively. All these values are percentages to the actual image.


## Model Diagram
### RetinaNet
<p align="center"><img src="https://miro.medium.com/max/2000/1*0-GVAp6WCzPMR6puuaYQTQ.png"></p>

### YOLOv3
<p align="center"><img src="https://miro.medium.com/max/2000/1*d4Eg17IVJ0L41e7CTWLLSg.png"></p>

### Faster-RCNN
<p align="center"><img src="https://tryolabs.com/images/blog/post-images/2018-01-18-faster-rcnn/fasterrcnn-architecture.b9035cba.png"></p>


## Pre-Trained Models
The Pre-Trained models can be downloaded from [google drive](https://drive.google.com/drive/folders/1QsNpLBR_g7ELBhJp404Ei0mEDjyJi8wx).

## Installation
## RetinaNet
```
 conda create -n Train python=3.7
 pip install -r code/keras-retinanet/requirements.txt
```
## YOLOv3
```
 conda create -n ACV2YOLO python=3.6
 conda install -c anaconda tensorflow-gpu
 pip install Pillow==2.2.1
 pip instal numpy
```
## Faster RCNN
```
 conda create -n FRCNN python=3.7
 conda install -c anaconda tensorflow-gpu
 pip install -r code/keras-frcnn/requirements.txt
```

## Training
To start training run the following command:
```
 source train.sh
```

## Testing
To start testing run the following command:
```
 source test.sh
```

## Quantitatvie Results
Results Reported on Private Leaderboard of Challenge

| Model | MAP 
| ----- | ---- 
| RetinaNet | 73 

## Results


## Author
`Maintainer` [Syed Nauyan Rashid](https://github.com/nauyan) (nauyan@hotmail.com)

## Acknowledgements
- [Implementation of RetinaNet in Keras](https://github.com/fizyr/keras-retinanet)
- [Implementation of YOLO3 in Keras](https://github.com/qqwweee/keras-yolo3)
- [Implementation of Faster-RCNN in Keras](https://github.com/kbardool/keras-frcnn)
