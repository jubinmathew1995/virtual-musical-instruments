import time
import random
import numpy as np
import cv2
import keras
from threading import Thread
from keras.models import model_from_json
import requests

from socketIO_client import SocketIO
socketIO = SocketIO('localhost', 8000)

SIZE_BOUNDING_SQUARE = 300
FILEPATH ="/home/jubin/Videos/new_data_from_real_time/"
MODEL_JSON = "/home/himanshu/Desktop/ml/models/Long_key_layout/v2_50e_reinf1/model.json"
MODEL_WEIGHTS = "/home/himanshu/Desktop/ml/models/Long_key_layout/v2_50e_reinf1/model.h5"
VIDEO_FEED = 1
CLASSNAME = 0
LINE_WIDTH = 2

ANS='00000'
PREV_ANS=ANS
PRESSED = False

def real_time_log():
    global ANS, PRESSED
    t = time.time()
    ##########
    # f = open("model.json", "r")
    # json_string = f.read()
    # f.close()
    ##########
    ### OR ###
    ##########
    with open(MODEL_JSON, "r") as f:
        json_string = f.read()
    ##########
    loaded_model = keras.models.model_from_json(json_string) 
    loaded_model.load_weights(MODEL_WEIGHTS)
    loaded_model.compile(loss=keras.losses.categorical_crossentropy,
                optimizer=keras.optimizers.Adadelta(),
                metrics=['accuracy'])
    print("\n"+'*'*40,"\nTRAINED MODEL LOADED IN", time.time() - t, "sec.\n"+'*'*40,"\n")

    START_PREDICTING_FLAG = False

    cap = cv2.VideoCapture(VIDEO_FEED)

    # for logging the frame rate.
    # t = time.time()
    # frame_cnt = 0
    while True:
        ret, frame = cap.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # increase the sleep time to decrease the frame rate.
        ## NO SLEEP - time.sleep(0.0)  - 24 frames/sec
        ## 0.05 sec - time.sleep(0.05) - 10 frames/sec
        ## 0.06 sec - time.sleep(0.06) - 9 frames/sec [ BEST - may be ]
        ## 0.07 sec - time.sleep(0.07) - 8 frames/sec
        ## 0.08 sec - time.sleep(0.08) - 8 frames/sec
        ## 0.1 sec  - time.sleep(0.1)  - 7 frames/sec
        # time.sleep(0.06)
        
        # for logging the frame rate.
        # frame_cnt += 1
        # cur_time = time.time()
        # print("Frame Rate =>", int(frame_cnt / (cur_time-t)), "frames/sec")

        # for generating the bounding box and cropping the image
        mid_width = int(frame.shape[1] / 2)
        mid_height = int(frame.shape[0] / 2)
        top_left = ((mid_width-int(SIZE_BOUNDING_SQUARE/2)), (mid_height+30))
        bottom_right = ((mid_width+int(SIZE_BOUNDING_SQUARE/2)), (mid_height+int(SIZE_BOUNDING_SQUARE/2)))
        top_left_new = ((mid_width-int(SIZE_BOUNDING_SQUARE/2)), (mid_height-int(SIZE_BOUNDING_SQUARE/2)))

        smallImg = np.array(frame[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]])

        cv2.rectangle(frame,top_left_new,bottom_right,(255,255,255), LINE_WIDTH)
        cv2.rectangle(frame,top_left,bottom_right,(0,255,0), LINE_WIDTH)

        if START_PREDICTING_FLAG:
            # cv2.imwrite("/home/jubin/"+str(time.time())+".png", smallImg)
            # img = cv2.resize(smallImg, (150, 150))
            x_test = np.array([smallImg])
            x_test = x_test.reshape(x_test.shape[0], 120, 300, 3)
            x_test = x_test.astype('float32')
            x_test /= 255
            res = loaded_model.predict(x_test)
            ans = (res>.7).astype(int).reshape(-1)
            temp = str(ans[1]) + str(ans[4]) + str(ans[2]) + str(ans[5]) + str(ans[3])
            ans=''.join([str(x) for x in ans[1:]])
            print(ans, PRESSED)
            # if ANS == ans:
            #     PRESSED = True
            # else:
            #     PRESSED = False
            # if (PRESSED == True):
            # requests.get('http://localhost:8000/'+str(ANS))
            if ANS != ans:
                socketIO.emit('msg_backend', temp)
            ANS = ans

            # if not PRESSED:
            #     sio.emit("data", ans)

        # for showing the video feed.
        cv2.imshow('frame', frame)
        k = cv2.waitKey(33)
        # print(k)
        if k == 27:
            break
        elif k == 32:
            START_PREDICTING_FLAG = not START_PREDICTING_FLAG
        elif k==48:
            print(k)
            # classname = 0
            CLASSNAME = str(0)
        elif k==49:
            # classname = 1
            CLASSNAME = str(1)
        elif k==50:
            # classname = 2
            CLASSNAME = str(2)
        elif k==51:
            # classname = 3
            CLASSNAME = str(3)
        elif k==52:
            # classname = 3
            CLASSNAME = str(4)
        elif k==53:
            # classname = 3
            CLASSNAME = str(5)
        elif k==83 or k==115:
            # for saving the image
            print("saving to: ", CLASSNAME)
            name = FILEPATH+CLASSNAME+"/"+str(time.time())+".png"
            cv2.imwrite(name, smallImg)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # t=Thread(target=real_time_log,args=())
    # t.start()
    real_time_log()