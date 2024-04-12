#! /bin/bash

model="frcnn"

 
if [ "${model,,}" == "retina" ] 
then
    echo "RETINA"
	conda activate Train
	#CUDA_VISIBLE_DEVICES=0 python code/keras-retinanet/test.py -p dataset/SIMS/images/
	conda deactivate
	
elif [ "${model,,}" == "frcnn" ]
then
    echo "FRCNN"
	conda activate FRCNN
	CUDA_VISIBLE_DEVICES=0 python code/keras-frcnn/test_frcnn.py -p dataset/SIMS/images/
	conda deactivate
	
elif [ "${model,,}" == "yolo" ]
then
    echo "YOLO"
	conda activate ACV2YOLO
	CUDA_VISIBLE_DEVICES=0  python code/keras-yolo3/test.py --model logs/000/trained_weights_final.h5 --anchors code/keras-yolo3/model_data/yolo_anchors.txt --classes classes_names.txt --gpu_num 1 --path dataset/SIMS/images/
	conda deactivate
else
    echo "Select Valid Model"
fi
