import glob
import cv2
import os
import pandas as pd

os.environ["CUDA_VISIBLE_DEVICES"] = "1"
dataset_path = "./dataset/SIMS"
Train = pd.read_csv(dataset_path+"/train.txt",header = None)
#print(Train)
Vald = pd.read_csv(dataset_path+"/vald.txt",header = None)
#print(Vald)
Test = pd.read_csv(dataset_path+"/test.txt",header = None)
#print(Test)



Train = Train.values
Vald = Vald.values
Test = Test.values
image_height = 768
image_width = 1024

columns=['filename','x1','y1','x2','y2','class_name']
columns_annotations=['class_idx','x','y','w','h']
class_names=['Car', 'Truck', 'Van', 'LongVehicle', 'Bus', 'Airliner', 'PropellerAircraft', 
    'TrainerAircraft', 'CharteredAircraft', 'FighterAircraft', 'Others', 'StairTruck',
    'PushbackTruck', 'Helicopter', 'Boat']
class_idx=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
map_dict = {0: "Car",1: "Truck",2: "Van",3: "LongVehicle",4: "Bus",5: "Airliner",6: "PropellerAircraft",
    7: "TrainerAircraft",8: "CharteredAircraft",9: "FighterAircraft",10: "Others",11: "StairTruck",
    12: "PushbackTruck",13: "Helicopter",14: "Boat"}

print("Generating Annotation File For Train Set")
training_set = pd.DataFrame(columns=columns)
for Train in Train:
    #print(dataset_path+Train[0][1:-4])
    example_path = dataset_path+Train[0][1:-4]
    img_path = glob.glob(example_path+".jpg")
    annot_path = glob.glob(example_path+".txt")
    annotation = pd.read_csv(annot_path[0],header = None, delimiter=r"\s+", names=columns_annotations)
    annotation['filename'] = img_path[0]
    annotation['x1'] = (annotation['x']-(annotation['w']/2))*image_width
    annotation['y1'] = (annotation['y']-(annotation['h']/2))*image_height
    annotation['x2'] = (annotation['x']+(annotation['w']/2))*image_width
    annotation['y2'] = (annotation['y']+(annotation['h']/2))*image_height
    annotation["class_name"] = annotation["class_idx"].map(map_dict)
    #annotation["class_name"] = annotation["class_idx"]
    annotation = annotation.drop(columns=['class_idx','x','y','w','h'])
    annotation = annotation[columns]
    training_set = training_set.append(annotation, ignore_index = True)
training_set['x1'] = training_set['x1'].astype('int32')  
training_set['y1'] = training_set['y1'].astype('int32')  
training_set['x2'] = training_set['x2'].astype('int32')  
training_set['y2'] = training_set['y2'].astype('int32')   
training_set.to_csv('./train.txt', index=False, header=False)
#print(training_set.dtypes)

print("Generating Annotation File For Vald Set")
validation_set = pd.DataFrame(columns=columns)
for Vald in Vald:
    #print(dataset_path+Vald[0][1:-4])
    example_path = dataset_path+Vald[0][1:-4]
    img_path = glob.glob(example_path+".jpg")
    annot_path = glob.glob(example_path+".txt")
    annotation = pd.read_csv(annot_path[0],header = None, delimiter=r"\s+", names=columns_annotations)
    annotation['filename'] = img_path[0]
    annotation['x1'] = (annotation['x']-(annotation['w']/2))*image_width
    annotation['y1'] = (annotation['y']-(annotation['h']/2))*image_height
    annotation['x2'] = (annotation['x']+(annotation['w']/2))*image_width
    annotation['y2'] = (annotation['y']+(annotation['h']/2))*image_height
    annotation["class_name"] = annotation["class_idx"].map(map_dict)
    #annotation["class_name"] = annotation["class_idx"]
    annotation = annotation.drop(columns=['class_idx','x','y','w','h'])
    annotation = annotation[columns]
    validation_set = validation_set.append(annotation, ignore_index = True) 
validation_set['x1'] = validation_set['x1'].astype('int32')  
validation_set['y1'] = validation_set['y1'].astype('int32')  
validation_set['x2'] = validation_set['x2'].astype('int32')  
validation_set['y2'] = validation_set['y2'].astype('int32')    
validation_set.to_csv('./vald.txt', index=False, header=False)
#print(validation_set.dtypes)

print("Generating Annotation File For Test Set")
testing_set = pd.DataFrame(columns=columns)
for Test in Test:
    #print(dataset_path+Test[0][1:-4])
    example_path = dataset_path+Test[0][1:-4]
    img_path = glob.glob(example_path+".jpg")
    annot_path = glob.glob(example_path+".txt")
    annotation = pd.read_csv(annot_path[0],header = None, delimiter=r"\s+", names=columns_annotations)
    annotation['filename'] = img_path[0]
    annotation['x1'] = (annotation['x']-(annotation['w']/2))*image_width
    annotation['y1'] = (annotation['y']-(annotation['h']/2))*image_height
    annotation['x2'] = (annotation['x']+(annotation['w']/2))*image_width
    annotation['y2'] = (annotation['y']+(annotation['h']/2))*image_height
    annotation["class_name"] = annotation["class_idx"].map(map_dict)
    #annotation["class_name"] = annotation["class_idx"]
    annotation = annotation.drop(columns=['class_idx','x','y','w','h'])
    annotation = annotation[columns]
    testing_set = testing_set.append(annotation, ignore_index = True) 
testing_set['x1'] = testing_set['x1'].astype('int32')  
testing_set['y1'] = testing_set['y1'].astype('int32')  
testing_set['x2'] = testing_set['x2'].astype('int32')  
testing_set['y2'] = testing_set['y2'].astype('int32')  
testing_set.to_csv('./test.txt', index=False, header=False)
#print(testing_set.dtypes)



