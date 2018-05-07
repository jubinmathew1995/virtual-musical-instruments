import os
import cv2
import random

raw_data = "/home/himanshu/Desktop/ml/raw_data/"
test_split = 0.10

data = '/home/himanshu/Desktop/ml/data/'
if not os.path.exists(data):
    os.makedirs(data)
if not os.path.exists(data+'test'):
    os.makedirs(data+'test')
if not os.path.exists(data+'train'):
    os.makedirs(data+'train')

for label in os.listdir(raw_data):
    # print(label)
    names = []
    for img in os.listdir(raw_data+label+'/'):
        names.append([raw_data+label+'/'+img, img])
    test_index = random.sample(range(0, len(names)), int(test_split*len(names)))
    # print(names)
    # print(test_index)
    if not os.path.exists(data+'test/'+label):
        os.makedirs(data+'test/'+label)
    if not os.path.exists(data+'train/'+label):
        os.makedirs(data+'train/'+label)
    for index in range(0, len(names)):
        loaded_img = cv2.imread(names[index][0])
        scaled_img = cv2.resize(loaded_img, (150, 150)) 
        if(index in test_index):
            cv2.imwrite(data+'test'+'/'+label+'/'+names[index][1], scaled_img)
        else:
            cv2.imwrite(data+'train'+'/'+label+'/'+names[index][1], scaled_img)

