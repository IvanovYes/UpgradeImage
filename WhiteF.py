from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import math

def CalculateHistogramm(imageL):
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    hist = np.zeros(256)
    for m in range(0, colums - 1, 1):
        for n in range(0, rows - 1, 1):
            hist[imageL[m, n]] = hist[imageL[m, n]] + 1
    return hist

def ContrustUp(imageL):
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    imageSize = colums * rows
    hist = CalculateHistogramm(imageL)
    H = np.zeros(256)
    H[0] = hist[0]
    for i in range(1, 255, 1):
        H[i] = H[i-1] + hist[i]
    Hmin = min(H)
    I = np.zeros(256)
    for i in range(0, 255, 1):
        I[i] = round(((H[i]-Hmin)/(imageSize - 1)) * 255)
        print(I[i])
    for m in range(0, colums - 1, 1):
        for n in range(0, rows - 1, 1):
            imageL[m, n] = I[imageL[m, n]]
    return imageL

imageL = cv.imread("C:/Users/ACER1/Pictures/alternative-beautiful.jpg", 1)
cv.imshow('', imageL)
cv.waitKey()

# Применение фильтрации для убирания шумов на изображении
imageL = cv.bilateralFilter(imageL, 3, 75, 75)

colums = imageL.shape[0]
rows = imageL.shape[1]
imageSize = colums * rows
imageL = cv.cvtColor(imageL, cv.COLOR_BGR2HSV)
hist = CalculateHistogramm(imageL[:, :, 2])
H = np.zeros(256)
H[0] = hist[0]
for i in range(1, 255, 1):
    H[i] = H[i-1] + hist[i]
Hmin = min(H)
I = np.zeros(256)
for i in range(0, 255, 1):
    I[i] = round(((H[i]-Hmin)/(imageSize - 1)) * 255)
for m in range(0, colums - 1, 1):
    for n in range(0, rows - 1, 1):
        imageL[m, n, 2] = I[imageL[m, n, 2]]

imageL = cv.cvtColor(imageL, cv.COLOR_HSV2BGR)

cv.imshow('', imageL)
cv.waitKey()

# Вызов функции баланса белого
image = BalanceWhight(image)
cv.imshow('', image)
cv.waitKey()