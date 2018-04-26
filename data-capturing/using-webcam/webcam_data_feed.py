import numpy as np
import cv2
import time

SIZE_BOUNDING_SQUARE = 400
cap = cv2.VideoCapture(0)

t = time.time()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    cur_time = time.time()


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    # for generating the bounding box and cropping the image
    print(gray.shape)
    mid_width = int(gray.shape[0] / 2)
    mid_height = int(gray.shape[1] / 2)
    top_left = ((mid_height-int(SIZE_BOUNDING_SQUARE/2)),
    			(mid_width-int(SIZE_BOUNDING_SQUARE/2)))
    bottom_right = ((mid_height+int(SIZE_BOUNDING_SQUARE/2)),
    			(mid_width+int(SIZE_BOUNDING_SQUARE/2)))
    # print(top_left)
    # print(bottom_right)
    smallImg = gray[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
    cv2.rectangle(gray,top_left,bottom_right,(255,0,0),3)

    # for saving the cropped images
    

    # Display the resulting frame
    cv2.imshow('cropped image', smallImg)
    cv2.imshow('frame',gray)
    k = cv2.waitKey(33)
    if k == 27:
        break
    elif k == 32:
    	cv2.imwrite("a"+str(cur_time-t)+".png", smallImg)
    	# break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()