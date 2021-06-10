import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
# disparity.py
def getDisparityMap(imL, imR, numDisparities, blockSize):
    stereo = cv2.StereoBM_create(numDisparities=numDisparities, blockSize=blockSize)

    disparity = stereo.compute(imL, imR)
    disparity = disparity - disparity.min() + 1  # Add 1 so we don't get a zero depth, later
    disparity = disparity.astype(
        np.float32) / 16.0  # Map is fixed point int with 4 fractional bits    return disparity # floating point image
    return disparity

# ================================================

# ================================================
def plot(disparity):
    # This just plots some sample points.  Change this function to
    # plot the 3D reconstruction from the disparity map and other values
    x = []
    y = []
    z = []
    height, width = disparity.shape

    baseline = 174.019  # mm
    doffs = 114.291  # resolution
    focus_len = 5806.559  # resolution

    for r in range(height):
        for c in range(width):
            if(disparity[r][c]<0.1): continue
            depth = baseline * focus_len / (disparity[r][c] + doffs)
            z += [depth]
            x += [c / focus_len * depth - baseline/2]
            y += [r / focus_len * depth]
    # Plt depths
    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, 'green', 1)

    # Labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # plt.savefig('myplot.pdf', bbox_inches='tight') # Can also specify an image, e.g. myplot.png
    plt.show()

def change(x):
    num = cv2.getTrackbarPos("num", "Disparity") * 16
    blockSize = (int)(cv2.getTrackbarPos("blockSize", "Disparity") / 2) * 2 + 1
    if (blockSize < 5):
        blockSize = 5
        # Get disparity map
    disparity = getDisparityMap(imgL, imgR, num, blockSize)

    disparityImg = np.interp(disparity, (disparity.min(), disparity.max()), (0.0, 1.0))
    cv2.imshow('Disparity', disparityImg)
    print(num, " ", blockSize)
    # plot(disparity)

if __name__ == '__main__':
    # 60 150
    minVal = 60
    maxVal = 150
    # Load left image
    filename = "umbrellaL.png"
    imgL = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    imgL = cv2.Canny(imgL,minVal,maxVal)
    cv2.imwrite('umbrellaL_edge.png',imgL)
    #
    if imgL is None:
        print('\nError: failed to open {}.\n'.format(filename))
        sys.exit()

    # Load right image
    filename = 'umbrellaR.png'
    imgR = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    imgR = cv2.Canny(imgR,minVal,maxVal)
    cv2.imwrite('umbrellaR_edge.png', imgR)
    #
    if imgR is None:
        print('\nError: failed to open {}.\n'.format(filename))
        sys.exit()

    # Create a window to display the image in
    cv2.namedWindow('Disparity', cv2.WINDOW_NORMAL)

    disparity = getDisparityMap(imgL, imgR, 80, 5)

    disparityImg = np.interp(disparity, (disparity.min(), disparity.max()), (0.0, 1.0))

    cv2.imshow('Disparity', disparityImg)  # Show initial image
    cv2.createTrackbar('num', 'Disparity', 2, 10, change)
    cv2.createTrackbar('blockSize', 'Disparity', 0, 31, change)

    plot(disparity)

    while True:
        key = cv2.waitKey(1)
        if key == ord(' ') or key == 27:
            break

    cv2.destroyAllWindows()
