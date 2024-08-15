from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv
import math

def CalculateHistogramm(imageL):
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    hist = np.zeros(256)
    for m in range(colums):
        for n in range(rows):
            hist[imageL[m, n]] = hist[imageL[m, n]] + 1
    return hist

def BalanceWhight(imageL):
    cLeft = np.zeros(3)
    cRight = np.zeros(3)
    for k in range(0, 2, 1):
        hist = CalculateHistogramm(imageL[..., k])
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

    f = np.zeros(256)
    colums = imageL.shape[0]
    rows = imageL.shape[1]
    for k in range(0, 2, 1):
        for c in range(0, 255, 1):
            f[c] = (round(((c - cLeft[k]) * 255 / (cRight[k] - cLeft[k]))))
            if f[c] > 255:
                f[c] = 255
            elif f[c] < 0:
                f[c] = 0
            print(f[c])
        for m in range(colums):
            for n in range(rows):
                imageL[m, n, k] = f[imageL[m, n, k]]
    return imageL

if __name__ == "__main__":

    # Считываем изображение
    image = cv.imread("C:/Users/ACER1/Pictures/Vika2.jpg", 1)
    cv.imshow('', image)
    print(image.shape)
    cv.waitKey()

    # Применение фильтрации для убирания шумов на изображении
    image = cv.bilateralFilter(image, 3, 75, 75)
    cv.imshow('', image)
    cv.waitKey()

    # Вызов функции баланса белого
    image = BalanceWhight(image)
    cv.imshow('', image)
    cv.waitKey()

    #Увеличение резкости изображения
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image = cv.filter2D(image, -1, kernel)
    image = cv.bilateralFilter(image, 5, 75, 75)
    cv.imshow('MyPhoto', image)
    cv.waitKey(0)

    isWritten = cv.imwrite('C:/Users/ACER1/Pictures/Vika1new.jpg', image)

    if isWritten:
        print('Image is successfully saved as file.')
    pass