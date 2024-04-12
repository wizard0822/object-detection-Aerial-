import pandas as pd

dataset_path = "./dataset/SIMS"
Train = pd.read_csv(dataset_path+"/training.txt")
#print(Train)
Vald = pd.read_csv(dataset_path+"/validation.txt")
#print(Vald)

Train = Train.values
Vald  =  Vald.values

training_set = []
for Train in Train:
    #print(dataset_path+Train[0][1:-4])
    #print(Train[0][:8]+"/"+Train[0][8:])
    training_set.append(Train[0][:8]+"/"+Train[0][8:])
training_set = pd.DataFrame(training_set) 
training_set.to_csv(dataset_path+'/train.txt', index=False, header=False)
    


validation_set = []
for Vald in Vald:
    #print(dataset_path+Vald[0][1:-4])
    #print(Vald[0][:8]+"/"+Vald[0][8:])
    validation_set.append(Vald[0][:8]+"/"+Vald[0][8:])
validation_set = pd.DataFrame(validation_set) 
validation_set.to_csv(dataset_path+'/vald.txt', index=False, header=False)
