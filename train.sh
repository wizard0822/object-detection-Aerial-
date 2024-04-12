#! /bin/bash

model="frcnn"

 
if [ "${model,,}" == "retina" ] 
then
    echo "RETINA"
	conda activate Train
	CUDA_VISIBLE_DEVICES=0 python code/keras-retinanet/keras_retinanet/bin/train.py csv train.txt classes.txt --val-annotations vald.txt
	conda deactivate
	
elif [ "${model,,}" == "frcnn" ]
then
    echo "FRCNN"
	conda activate FRCNN
	CUDA_VISIBLE_DEVICES=0 python code/keras-frcnn/train_frcnn.py -o simple -p all_data.txt
	conda deactivate
	
elif [ "${model,,}" == "yolo" ]
then
    echo "YOLO"
	conda activate ACV2YOLO
	CUDA_VISIBLE_DEVICES=0 python code/keras-yolo3/train.py
	conda deactivate
else
    echo "Select Valid Model"
fi





