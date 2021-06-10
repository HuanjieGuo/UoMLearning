# Based on https://docs.opencv.org/3.4/dc/dbb/tutorial_py_calibration.html
# T. Morley, The University of Manchester, 08 Jan 2020

import numpy as np
import cv2 as cv
import glob
import sys

# Get command line arguments
numArgs = len(sys.argv)

if numArgs < 3:
    print("\nError: not enough arguments.")
    print('Usage:')
    print('python3 undistort.py image_file model_name')
    print('\nExample:')
    print('python3 undistort.py test.jpg canon18mm')
    print('\nCalibration parameters will then be loaded from files')
    print('  canon18mm_matrix.txt and canon18mm_distortion.txt')
    print()
    sys.exit()

file_name = sys.argv[1] # e.g. 'test.jpg'
model_name = sys.argv[2] # e.g. 'canon18mm'


mtx = np.loadtxt('%s_matrix.txt' % model_name)
dist = np.loadtxt('%s_distortion.txt' % model_name)

print('\n matrix =', mtx)
print('distortion =', dist)

img = cv.imread(file_name)
h = img.shape[0]
w = img.shape[1]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

print('Region of interest =', roi)

# NOTE
# If roi comes out as all zeros, use different calibration images in the cal
# making sure that there are lots of corners near to the edge of the images
# where the distortion is worse.

# undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)

# crop the image
x, y, w, h = roi
#dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult.jpg', dst)
