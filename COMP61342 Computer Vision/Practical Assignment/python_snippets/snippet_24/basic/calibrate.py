# Based on https://docs.opencv.org/3.4/dc/dbb/tutorial_py_calibration.html
# T. Morley, The University of Manchester, 08 Jan 2020

import numpy as np
import cv2 as cv
import glob
import sys

# If chessboard is 10x7 squares then internal_corners is 9x6:
internal_corners = (9,6)


# Get command line arguments
numArgs = len(sys.argv)

if numArgs < 3:
    print("\nError: not enough arguments.")
    print('Usage:')
    print('python3 calibrate.py image_filter model_name')
    print('\nExample:')
    print('python3 calibrate.py \'calimgs/*.jpg\' canon18mm')
    print('\nCalibration parameters will then be saved in files')
    print('  canon18mm_matrix.txt and canon18mm_distortion.txt')
    print("\nNOTE: don't forget to put quotes around the file filter so that the shell doesn't expand it")
    print()
    sys.exit()

file_filter = sys.argv[1] # e.g. 'canon_18mm_cal/*.JPG'
model_name = sys.argv[2] # e.g. 'canon18mm'


# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((internal_corners[0]*internal_corners[1],3), np.float32)
objp[:,:2] = np.mgrid[0:internal_corners[0],0:internal_corners[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Process set of chessboard images
images = glob.glob(file_filter)

if len(images) <= 0:
    print('No images found for filter:', file_filter)
    sys.exit()

for fname in images:
    print('Processing', fname)
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, internal_corners, None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        print('  Found corners')
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        #cv.imshow('img', img)
        #cv.waitKey(500)
    else:
        print('  Failed to find corners')

cv.destroyAllWindows()

# Perform calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, \
        gray.shape, None, None)

# Save matrix and distortion values for later use
np.savetxt('%s_matrix.txt' % model_name, mtx)
np.savetxt('%s_distortion.txt' % model_name, dist)
