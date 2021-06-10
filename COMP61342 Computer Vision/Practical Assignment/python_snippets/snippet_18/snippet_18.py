# snippet_18.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Register images using ORB features.
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

    # Get the corresponding points for the good matches
    srcPoints = [kps2[matches[i].trainIdx].pt for i in range(len(matches))]
    dstPoints = [kps1[matches[i].queryIdx].pt for i in range(len(matches))]

    # Find Homography - a transformation to warp the object image
    H, _ = cv2.findHomography(np.array(srcPoints), np.array(dstPoints), cv2.RANSAC)

    # Warp the object image into the size of the main image
    out = cv2.warpPerspective(img2, H, (img1.shape[1], img1.shape[0]), flags=cv2.INTER_CUBIC)
    cv2.imwrite('warped.jpg', out)

    # Draw the outline of the object on the main image
    # (Uses homogeneous coordinates. @ = matrix multiplication)
    # Warp the four corners of the object image
    top_left = H @ np.array((0, 0, 1))
    top_right = H @ np.array((img2.shape[1], 0, 1))
    bot_right = H @ np.array((img2.shape[1], img2.shape[0], 1))
    bot_left = H @ np.array((0, img2.shape[0], 1))

    # Normalise and get rid of element 2
    top_left = (int(top_left[0] / top_left[2]), int(top_left[1] / top_left[2]))
    top_right = (int(top_right[0] / top_right[2]), int(top_right[1] / top_right[2]))
    bot_right = (int(bot_right[0] / bot_right[2]), int(bot_right[1] / bot_right[2]))
    bot_left = (int(bot_left[0] / bot_left[2]), int(bot_left[1] / bot_left[2]))
    #
    # Draw the outline
    out = img1.copy()
    out = cv2.line(out, top_left, top_right, (0, 0, 255))
    out = cv2.line(out, top_right, bot_right, (0, 0, 255))
    out = cv2.line(out, bot_right, bot_left, (0, 0, 255))
    out = cv2.line(out, bot_left, top_left, (0, 0, 255))
    cv2.imwrite('obj_outline.jpg', out)
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
