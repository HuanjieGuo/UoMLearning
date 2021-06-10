import cv2
import sys
import numpy as np
# disparity.py
def getDisparityMap(imL, imR, numDisparities, blockSize):
    stereo = cv2.StereoBM_create(numDisparities=numDisparities, blockSize=blockSize)

    disparity = stereo.compute(imL, imR)
    disparity = disparity - disparity.min() + 1  # Add 1 so we don't get a zero depth, later
    disparity = disparity.astype(
        np.float32) / 16.0  # Map is fixed point int with 4 fractional bits    return disparity # floating point image
    return disparity

def change(x):
    num = cv2.getTrackbarPos("num", "Disparity") * 16
    blockSize = (int)(cv2.getTrackbarPos("blockSize", "Disparity") / 2) * 2 + 1
    k = 0.5+cv2.getTrackbarPos("k", "Disparity")/100.0
    blur_time = cv2.getTrackbarPos("blur_time","Disparity")
    thres = cv2.getTrackbarPos("threshold","Disparity")/100
    if (blockSize < 5):
        blockSize = 5
        # Get disparity map
    disparity = getDisparityMap(imgL, imgR, num, blockSize)
    for _ in range(0,blur_time):
        disparity = cv2.medianBlur(disparity,5)
    disparityImg = np.interp(disparity, (disparity.min(), disparity.max()), (0.0, 1.0))
    depth = depthMap(disparityImg,k)
    depth = np.interp(depth, (depth.min(), depth.max()), (0.0, 1.0))

    raw,col = depth.shape
    for i in range(0,raw):
        for j in range(0,col):
            if(depth[i][j]>thres):
                depth[i][j] = 1
    cv2.imshow('Disparity', depth)
    greyHeavyBlur(depth)
    colorHeavyBlur(depth)
    colorGreyBG(depth)
    print("num: ",num, " blockSize: ", blockSize," k=",k," blur_time:",blur_time," threhold:",thres)
'''
num:  16  blockSize:  15  k= 0.61  blur_time: 10  threshold: 1
num:  16  blockSize:  31  k= 0.61  blur_time: 10  threhold: 0.86
'''
def greyHeavyBlur(depth):
    filename = 'girlL.png'
    oriImg = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img = cv2.blur(oriImg,(20,20))
    height,width = depth.shape
    for raw in range(0,height):
        for col in range(0,width):
            if(depth[raw][col]!=1):
                img[raw][col] = oriImg[raw][col]
    cv2.imshow('GreyHeavyBlur', img)

def colorHeavyBlur(depth):
    filename = 'girlL.png'
    oriImg = cv2.imread(filename, cv2.COLOR_RGB2GRAY)
    img = cv2.blur(oriImg, (20, 20))
    height, width = depth.shape
    for raw in range(0, height):
        for col in range(0, width):
            if (depth[raw][col] != 1):
                img[raw][col] = oriImg[raw][col]
    cv2.imshow('ColorHeavyBlur', img)

def colorGreyBG(depth):
    filename = 'girlL.png'
    colorImg = cv2.imread(filename, cv2.COLOR_RGB2GRAY)
    greyImg = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    height, width = depth.shape
    for raw in range(0, height):
        for col in range(0, width):
            if (depth[raw][col] == 1):
                colorImg[raw][col] = greyImg[raw][col]*np.ones(3)
    cv2.imshow('ColorGreyBG', colorImg)

def depthMap(disparity,k):
    return 1/(disparity+k)

if __name__ == '__main__':
    # Load left image
    filename = "girlL.png"
    imgL = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    #
    if imgL is None:
        print('\nError: failed to open {}.\n'.format(filename))
        sys.exit()

    # Load right image
    filename = 'girlR.png'
    imgR = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    #
    if imgR is None:
        print('\nError: failed to open {}.\n'.format(filename))
        sys.exit()
    # Create a window to display the image in
    cv2.namedWindow('Disparity', cv2.WINDOW_NORMAL)
    cv2.namedWindow('GreyHeavyBlur', cv2.WINDOW_NORMAL)
    cv2.namedWindow('ColorHeavyBlur', cv2.WINDOW_NORMAL)
    cv2.namedWindow('ColorGreyBG', cv2.WINDOW_NORMAL)

    disparity = getDisparityMap(imgL, imgR, 64, 9)
    # Normalise for display
    disparityImg = np.interp(disparity, (disparity.min(), disparity.max()), (0.0, 1.0))

    # Show result
    cv2.imshow('Disparity', disparityImg)

    cv2.createTrackbar('num', 'Disparity', 2, 10, change)
    cv2.createTrackbar('blockSize', 'Disparity', 0, 31, change)
    cv2.createTrackbar('k', 'Disparity', 0, 100, change)
    cv2.createTrackbar('blur_time','Disparity',0,10,change)
    cv2.createTrackbar('threshold','Disparity',100,100,change)

    while True:
        key = cv2.waitKey(1)
        if key == ord(' ') or key == 27:
            break

    cv2.destroyAllWindows()