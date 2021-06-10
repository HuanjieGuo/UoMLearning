# snippet_26.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Create a disparity map for stereo images.
 """

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Source: https://www.docs.opencv.org/master/dd/d53/tutorial_py_depthmap.html

# Globals
gNumDisparities = 16
gBlockSize = 5
imgL = None
imgR = None


# ================================================
# Callback function to receive messages from the TrackBar
def changeDisp(x):
    global gNumDisparities

    # numDisparities must be multiple of 16

    gNumDisparities = 16 * (x + 1)

    displayResult()
# ================================================


# ================================================
# Callback function to receive messages from the TrackBar
def changeBlock(x):
    global gBlockSize

    # blockSize must be odd
    gBlockSize = 2 * x + 5

    displayResult()
# ================================================


# ================================================
# Callback function to receive messages from the TrackBar
def displayResult():
    #stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    stereo = cv2.StereoBM_create(numDisparities=gNumDisparities, blockSize=gBlockSize)

    disparity = stereo.compute(imgL,imgR)

    # Scale disparity values in range [0, 1]
    # which will be displayed as floating point image
    disparity = np.interp(disparity, (disparity.min(), disparity.max()), (0, 1))

    cv2.imshow('Display', disparity)
# ================================================



# ================================================
#
if __name__ == '__main__':

    # Load left and right images
    imgL = cv2.imread('shaft3recl.png',0)
    imgR = cv2.imread('shaft3recr.png',0)

    # Create a window to display the image in
    cv2.namedWindow('Display')
    displayResult()

    # Create TrackBars
    cv2.createTrackbar('numDisparities', 'Display', 0, 10, changeDisp)
    cv2.createTrackbar('blockSize', 'Display', 0, 20, changeBlock)

    # Wait for spacebar press or escape before closing,
    # otherwise window will close without you seeing it
    while True:
        key = cv2.waitKey(1)
        if key == ord(' ') or key == 27:
            break

    cv2.destroyAllWindows()

    print('Final values:')
    print('numDisparities =', gNumDisparities)
    print('blockSize =', gBlockSize)
