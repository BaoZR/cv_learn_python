# -*- coding=utf-8 -*-

# numpy process pixel

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("../resource/Lena.png")
print(type(img))

blue = img.item(78, 100, 0)









