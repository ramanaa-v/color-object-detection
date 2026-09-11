import numpy as np

import cv2


def get_limits(color):
    
    c = np.uint8([[color]]) # here insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_Limit = hsvC[0][0][0] - 10, 100, 100
    upper_Limit = hsvC[0][0][0] + 10, 255, 255

    lower_Limit = np.array(lower_Limit, dtype=np.uint8)
    upper_Limit = np.array(upper_Limit, dtype=np.uint8)
    return lower_Limit, upper_Limit