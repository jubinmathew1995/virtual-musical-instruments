from os import listdir, getcwd
import cv2
import numpy as np
from os.path import expanduser

FILEPATH = expanduser("~")

train_test = [ "/train", "/test"]
# p = 1
# up = 0
# print(listdir(FILEPATH))
for x in train_test:
	image_arr = []
	label_arr = []
	for i in listdir(FILEPATH+x):
		print(i)
		for j in listdir(FILEPATH+x+"/"+i):
			name = FILEPATH+x+"/"+i+"/"+j
			img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
			# print(img.shape)
			image_arr.append(img)
			label_arr.append(int(i))
	a = np.array(image_arr)
	b = np.array(label_arr)
	print(a.shape)
	print(b.shape)
	np.save(FILEPATH+"/x_"+x[1:], a)
	np.save(FILEPATH+"/y_"+x[1:], b)

# 		for k in listdir(i+j):
# 			# print(i+j+k)	
# 			name = i+j+k
# 			# print(name)
# 			img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
# 			img = img[:-8,:]
# 			print(img.shape)
# 			img = img.reshape((1, (img.shape[0] * img.shape[1])))
# 			image_arr.append(img[0])
# 			if j=="/p/":
# 				label_arr.append([1])
# 			else:
# 				label_arr.append([0])

# 	np.save(i+"/x", image_arr)
# 	# label_arr = np.transpose(label_arr)
# 	np.save(i+"/y", label_arr)
# 			# print(type(img))		
# 		# print(listdir(i+j))
# name ="/home/jubin/Desktop/training-images/y.npy"
# res = np.load(name)
# print(res.shape)
# name ="/home/jubin/Desktop/training-images/x.npy"
# res = np.load(name)
# print(res.shape)
# # img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
# # print(type(img))
# # # print(img)
# # # print("shape",img.shape)
# # updated_img = img.reshape((1, (img.shape[0] * img.shape[1])))
# # print(updated_img) 
# # print("shape",updated_img.shape)
# # img = cv2.reshape((1, 374528))
# # new = img[0].reshape(616, 608)
# # print(new.shape)
# # print("shape",img.shape)



