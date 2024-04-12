import os
os.remove("train_yolo.txt")
#print("File Removed!")

f = open("train.txt", "r")
f1 = open("train_yolo.txt", "a")
#f.write("Now the file has more content!")
for x in f:
  #print(x,x[:30]+" "+x[31:])
  print(x)
  f1.write(x[:30]+" "+x[31:])
f1.close()  
f.close()