# -*- coding:utf-8 -*-

# 演示修改指定位置的像素值，并做显示

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../resource/flower.png")
test = img[100, 100]
print("当前像素值:", test)

img[100, 100] = [255, 255, 255]
print("修改后的像素值:", test)

cv2.imshow("demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()








