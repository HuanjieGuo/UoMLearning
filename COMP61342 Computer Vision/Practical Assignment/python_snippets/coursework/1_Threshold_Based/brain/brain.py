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

def mamualSegBinary(img,thres,saveIfHigher):
    if saveIfHigher:
        _,img = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY)
    else:
        _,img = cv2.threshold(img, thres, 255, cv2.THRESH_BINARY_INV)
    print('Manual threhold is %s' % thres)
    note = None
    if saveIfHigher:
        note = "above"
    else:
        note="below"
    cv2.imshow(note+'_thres_'+ str(thres), img)
    cv2.imwrite(note+'_thres_'+ str(thres) + '.png', img)
    return img

def imgAND(img1,img2):
    height,width = img1.shape
    img = np.zeros([height,width])
    for raw in range(0,height):
        for col in range(0,width):
            if img1[raw][col]==255 and img2[raw][col]==255:
                img[raw][col] = 255
    cv2.imshow('AND', img)
    return img

def otsuSegImg(img):
    T, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    plt.imshow(img, cmap='gray')
    cv2.namedWindow('otsu_threshold_'+str(T), cv2.WINDOW_NORMAL)
    # Display image
    cv2.imshow('otsu_threshold_'+str(T),img)
    cv2.imwrite('otsu_thres_' + str(int(T)) + '.png', img)

if __name__ == '__main__':
    # Open JPEG image
    img = cv2.imread('brain.png', cv2.IMREAD_GRAYSCALE)

    # get image histogram
    # histogram(img)

    # manual binary segmentation
    thresAbove = 185
    imgAbove = mamualSegBinary(img.copy(),thresAbove,True)
    thresBelow = 220
    imgBelow = mamualSegBinary(img.copy(), thresBelow, False)
    andImg = imgAND(imgAbove,imgBelow)
    cv2.imwrite( 'thres_'+str(thresAbove)+'_'+str(thresBelow)+'.png', andImg)

    # get segmentation by otsu
    # otsuSegImg(img)

    # show origin img
    cv2.imshow('origin',img)

    while True:
        key = cv2.waitKey(1)
        if key == ord(' ') or key == 27:
            break

cv2.destroyAllWindows()
