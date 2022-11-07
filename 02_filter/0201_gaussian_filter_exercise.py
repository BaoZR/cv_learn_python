# -*- coding=utf-8 -*-
import cv2
import numpy as np


def my_gaussian_filter(img, K_size=3, sigma=1.3):
    # get image size
    if len(img.shape) == 3:
        H, W, C = img.shape
    else:
        img = np.expand_dims(img, axis=-1)
        H, W, C = img.shape

    # zero padding
    pad = K_size // 2
    out = np.zeros((H + pad * 2, W + pad * 2, C), dtype=float)
    out[pad: H+pad, pad: W+pad] = img.copy().astype(float)

    # prepare kernel
    K = np.zeros((K_size, K_size), dtype=float)
    # x y 如此取值的原因
    for x in range(-pad, -pad + K_size):
        for y in range(-pad, -pad + K_size):
            K[y + pad, x + pad] = np.exp(-(x ** 2 + y ** 2)/(2 * (sigma ** 2)))
    K /= (2 * np.pi * (sigma * sigma))
    K /= K.sum()

    tmp = out.copy()

    # filtering
    for y in range(H):
        for x in range(W):
            for c in range(C):
                out[pad + y, pad + x, c] = np.sum(K * tmp[y: y + K_size, x: x + K_size, c])

    out = np.clip(out, 0, 255)
    out = out[pad: pad + H, pad: pad + W].astype(np.uint8)

    return out


if __name__ == "__main__":
    img = cv2.imread("../resource/imori_noise.jpg")
    out = my_gaussian_filter(img, 3, 1.3)
    cv2.imshow("result", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
