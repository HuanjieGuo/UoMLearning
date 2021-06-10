# snippet_14.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Stitch images together.
"""

import cv2
import sys
import numpy as np


im1 = cv2.imread('stafford01.jpg')
im2 = cv2.imread('stafford02.jpg')

# Add the images into an array
images = []
images.append(im1)
images.append(im2)

# Stitch the images
stitcher = cv2.Stitcher_create(cv2.STITCHER_SCANS)
(status, stitched) = stitcher.stitch(images)

# Save result
filename = 'stitched.png'
print('Writing output file to ' + filename)
cv2.imwrite(filename, stitched)
