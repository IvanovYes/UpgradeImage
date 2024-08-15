from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import math

def ColculateHistogramm(imageL):
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    hist = np.zeros(256)
    for m in range(0, colums - 1, 1):
        for n in range(0, rows - 1, 1):
            hist[imageL[m, n]] = hist[imageL[m, n]] + 1
    return hist

imageL = cv.imread("C:/Users/ACER1/Pictures/alternative-beautiful.jpg", 1)

# Применение фильтрации для убирания шумов на изображении
imageL = cv.bilateralFilter(imageL, 5, 75, 75)

cv.imshow('', imageL)
cv.waitKey()


cLeft = np.zeros(3)
cRight = np.zeros(3)

for k in range(3):
    hist = ColculateHistogramm(imageL[..., k])
    for i in range(0, 255, 1):
        if hist[i] > 100:
            cLeft[k] = i
            break
            pass

    for i in range(0, 255, 1):
        if hist[255 - i] > 100:
            cRight[k] = 255 - i
            break
            pass

print(cLeft, cRight)
f = np.zeros(256)
colums = imageL.shape[0]
rows = imageL.shape[1]
for k in range(3):
    for c in range(0, 255, 1):
        f[c] = abs(round(((c - cLeft[k]) * 255 / (cRight[k] - cLeft[k]))))
    for m in range(0, colums - 1, 1):
        for n in range(0, rows - 1, 1):
            imageL[m, n, k] = f[imageL[m, n, k]]

imageL = cv.cvtColor(imageL, cv.COLOR_BGR2HSV)

for m in range(0, colums - 1, 1):
    for n in range(0, rows - 1, 1):
        imageL[m, n, 1] = 255

imageL = cv.cvtColor(imageL, cv.COLOR_HSV2BGR)
cv.imshow('', imageL)
cv.waitKey()