# -*- coding:utf-8 -*-

# 读图和用2*2的田字格显示图像

import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('../resource/flower.png')
img2 = cv2.imread('../resource/Lena.png')

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

titles = ['flower', 'lena', 'flower', 'lena']
images = [img1, img2, img1, img2]
for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()











