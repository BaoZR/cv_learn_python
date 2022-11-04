# -*- coding=utf-8 -*-

# 将指定区域设置为白色

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../resource/flower.png")
img[100:200, 120:200] = [255, 255, 255]
cv2.imshow("flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()








