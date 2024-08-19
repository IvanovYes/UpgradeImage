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
    channels = image.shape[2]
    for k in range(0, channels, 1):
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
    for k in range(0, channels, 1):
        for c in range(0, 255, 1):
            f[c] = (round(((c - cLeft[k]) * 255 / (cRight[k] - cLeft[k]))))
            if f[c] > 255:
                f[c] = 255
            elif f[c] < 0:
                f[c] = 0
        for m in range(colums):
            for n in range(rows):
                imageL[m, n, k] = f[imageL[m, n, k]]
    return imageL

if __name__ == "__main__":
    print("Введите путь к изображению (используйте прямой слэш): ")
    frame = input()
    # Считываем изображение
    imageOrig = cv.imread(frame, 1)

    # Применение фильтрации для убирания шумов на изображении
    image = cv.bilateralFilter(imageOrig, 3, 75, 75)

    # Вызов функции баланса белого
    image = BalanceWhight(image)

    # Увеличение резкости изображения
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image = cv.filter2D(image, -1, kernel)
    image = cv.bilateralFilter(image, 5, 75, 75)

    cv.imshow(' ', image)
    cv.waitKey(0)

    # Вывод обработанного изображения
    imageOrig = cv.cvtColor(imageOrig, cv.COLOR_BGR2RGB)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    fig, ax = plt.subplots(1, 2, figsize=(12, 4))

    ax[0].imshow(imageOrig)
    ax[0].set_title('Before')

    ax[1].imshow(image)
    ax[1].set_title('After')

    plt.show()
    pass