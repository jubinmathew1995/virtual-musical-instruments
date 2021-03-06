#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import time
from os.path import expanduser
import argparse
import os
import datetime

SIZE_BOUNDING_SQUARE = 400 # default cut window size
CLASSNAME = "1"
FILEPATH = expanduser("~")
SHOULD_SAVE = False


parser = argparse.ArgumentParser()
parser.add_argument("--classname","-c", help="classname of the current image (1-6), DEFAULT = 1")
parser.add_argument("--filepath", "-f", help="filepath where the data is to be saved , Default = ~/raw_data/")
parser.add_argument("--boxsize", "-b", help="size of the box which is to be cut, DEFAULT = 400")
args = parser.parse_args()

if args.classname:
    CLASSNAME = args.classname
if args.filepath:
    FILEPATH = args.filepath
if args.boxsize:
    SIZE_BOUNDING_SQUARE = int(args.boxsize)

FILEPATH += "/raw_data"
if not os.path.exists(FILEPATH):
    os.makedirs(FILEPATH)

FILEPATH += ("/"+CLASSNAME+"/")
if not os.path.exists(FILEPATH):
    os.makedirs(FILEPATH)

print(FILEPATH)

# cv2.namedWindow('Depth')
cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video()[0])

t = time.time()
frame_cnt = 0

while 1:
    # cv2.imshow('Depth', get_depth())
    gray = get_depth()
    cur_time = time.time()
    # y = get_depth()

    # increase the sleep time to decrease the frame rate.
    # time.sleep(0.1)

    # converting the image to grayscale 
#    gray = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)

    # for logging the stats
    frame_cnt += 1
    # print(x)
    cur_time = time.time()
    # cv2.imwrite("a"+str(cur_time-t)+".png", x)
    print("elapsed time =>", cur_time-t, "sec")
    print("no of frames", frame_cnt)

    # for generating the bounding box and cropping the image
    # print(gray.shape)
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

    if SHOULD_SAVE:
        tm = str(datetime.datetime.fromtimestamp(time.time()))
        tm = tm.replace(" ", '-')
        img_name = FILEPATH + CLASSNAME + "-" + tm

        cv2.imwrite(img_name + ".png", smallImg)

    # Display the resulting frame
    cv2.imshow('cropped image', smallImg)
    cv2.imshow('frame',gray)
    k = cv2.waitKey(33)
    if k == 27:
        break
    elif k == 32:
        SHOULD_SAVE = not SHOULD_SAVE
        # cv2.imwrite("a"+str(cur_time-t)+".png", smallImg)
        # break
