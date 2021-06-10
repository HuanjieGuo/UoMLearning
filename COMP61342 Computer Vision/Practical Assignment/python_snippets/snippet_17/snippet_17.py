# snippet_17.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Find and match image features using ORB.
"""

import cv2
import sys
import numpy as np


#############################################################
## findFeatures()
##
def matchFeatures(img1, img2):

    # Initiate feature detector: ORB
    fd = cv2.ORB_create(nfeatures=200) # Limit number of features found to 200

    # find the keypoints and descriptors with ORB
    kps1, descs1 = fd.detectAndCompute(img1, None)
    kps2, descs2 = fd.detectAndCompute(img2, None)

    # create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors.
    matches = bf.match(descs1, descs2)

    # Draw matches
    imgMatches = img1.copy()
    imgMatches = cv2.drawMatches(img1, kps1, img2, kps2, matches, imgMatches, flags=2)

    cv2.imwrite('matches.jpg', imgMatches)
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


    input_file = 'book.jpg'
    imgObj = cv2.imread(input_file)
    #
    # Check for success
    if imgObj is None:
        print('Failed to open', input_file)
        sys.exit()


    # Find the features in the image.
    matchFeatures(img, imgObj)
#############################################################
