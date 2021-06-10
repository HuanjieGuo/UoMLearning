import cv2
import matplotlib.pyplot as plt
import numpy as np

def histogram(img):
    # show histogram
    # Calculate the histogram
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    hist = hist.reshape(256)

    # Plot histogram
    plt.bar(np.linspace(0, 255, 256), hist)
    plt.title('Histogram')
    plt.ylabel('Frequency')
    plt.xlabel('Grey Level')
    plt.show()

if __name__ == '__main__':
    img = cv2.imread('tray.png', cv2.IMREAD_GRAYSCALE)
    # smooth
    blur = cv2.blur(img, (100, 100))
    cv2.imwrite('tray_blur.png', blur)

    # subtract and add it bac
    img = img - blur + 128
    cv2.imwrite('tray_final.png', img)

    # # threshold
    thres = 95
    # img = cv2.imread('tray.png', cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)
    cv2.imwrite('tray_thres_'+str(thres)+'.png', img)
