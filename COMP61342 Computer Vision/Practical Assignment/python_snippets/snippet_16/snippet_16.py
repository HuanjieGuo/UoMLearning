# snippet_16.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Find image features using ORB.
"""

import cv2
import sys
import numpy as np


#############################################################
## findFeatures()
##
def findFeatures(img):

    # Initiate feature detector: ORB
    fd = cv2.ORB_create(nfeatures=200) # Limit number of features found to 200

    # find the keypoints and descriptors with ORB
    kps, descs = fd.detectAndCompute(img, None)

    # Mark features with circles
    out = img.copy() # make a duplicate to draw on
    out = cv2.drawKeypoints(img, kps, out)
    cv2.imwrite('features1.jpg', out)

    # Mark features with their size and orientation
    out = img.copy() # make a duplicate to draw on
    out = cv2.drawKeypoints(img, kps, out, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite('features2.jpg', out)
#############################################################




#############################################################
## The main 'function'
##
if __name__ == '__main__':

    input_file = 'books.jpg'
    img = cv2.imread(input_file)
    #
    # Check for success
    if img is None:
        print('Failed to open', input_file)
        sys.exit()


    # Find the features in the image.
    findFeatures(img)
#############################################################
