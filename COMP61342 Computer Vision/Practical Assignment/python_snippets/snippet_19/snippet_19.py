# snippet_19.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: K-means clustering.

Source: https://docs.opencv.org/4.2.0/d1/d5c/tutorial_py_kmeans_opencv.html
    OpenCV-Python Tutorial: K-Means Clustering in OpenCV
"""

import cv2
import sys
import numpy as np


#############################################################
## kmeansColour()
##
def kmeansColour(img, K):

    Z = img.reshape((-1,3)) # changes an BGR image into a 1D array of BGR values
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label,center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    return res2
#############################################################



#############################################################
## kmeansIntensity()
##
def kmeansIntensity(img, K):

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);

    Z = grey.reshape((-1)) # changes an greyscale image into a 1D array of intensity values
    # convert to np.float32
    Z = np.float32(Z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    ret, label,center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((grey.shape))

    return res2
#############################################################




#############################################################
## The main 'function'
##
if __name__ == '__main__':

    # k-means colour ---------------------------
    input_file = 'veggies.png'
    img = cv2.imread(input_file)
    #
    # Check for success
    if img is None:
        print('Failed to open', input_file)
        sys.exit()

    # Perform k-means on colour.
    for k in (2, 4, 6, 8):
        out = kmeansColour(img, k)
        cv2.imwrite('veggies_k{}.jpg'.format(k), out)


    # k-means colour ---------------------------
    input_file = 'beach.jpg'
    img = cv2.imread(input_file)
    #
    # Check for success
    if img is None:
        print('Failed to open', input_file)
        sys.exit()

    # Perform k-means on colour.
    for k in (2, 4, 6, 8):
        out = kmeansColour(img, k)
        cv2.imwrite('beach{}.jpg'.format(k), out)


    # k-means intensity ---------------------------
    input_file = 'panda.png'
    img = cv2.imread(input_file)
    #
    # Check for success
    if img is None:
        print('Failed to open', input_file)
        sys.exit()

    # Perform k-means on intensity.
    for k in (2, 4, 6, 8):
        out = kmeansIntensity(img, k)
        cv2.imwrite('panda{}.jpg'.format(k), out)
#############################################################
