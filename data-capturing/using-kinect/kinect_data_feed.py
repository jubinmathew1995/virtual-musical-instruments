#!/usr/bin/env python
import freenect
import cv2
import frame_convert2
import time

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
    x = get_video()
    # y = get_depth()

    # increase the sleep time to decrease the frame rate.
    time.sleep(0.1)
    # x = cv2.cvtColor(x,cv2.COLOR_RGB2GRAY)

    # for logging the stats
    frame_cnt += 1
    print(x)
    cur_time = time.time()
    # cv2.imwrite("a"+str(cur_time-t)+".png", x)
    print("elapsed time =>", cur_time-t, "sec")
    print("no of frames", frame_cnt)

    cv2.imshow('Video', x)
    # cv2.imshow('Depth', y)
    if cv2.waitKey(10) == 27:
        break
