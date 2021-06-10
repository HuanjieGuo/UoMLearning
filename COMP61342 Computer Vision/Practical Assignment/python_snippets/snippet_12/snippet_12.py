# snippet_12.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Erode, dilate, open and close.
"""

import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np


input_file = 'white-blood-cells.jpg'
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()


# Threshold
_, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
cv2.imwrite('threshold.png', thresh)


# Create structuring element
struc_elem = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))


# Erode (a number of times)
output = thresh.copy()
for i in range(3):
    output = cv2.erode(output, struc_elem)
#
cv2.imwrite('eroded.png', output)


# Dilate (a number of times)
output = thresh.copy()
for i in range(3):
    output = cv2.dilate(output, struc_elem)
#
cv2.imwrite('dilated.png', output)


# Open (a number of times)
output = thresh.copy()
for i in range(6):
    output = cv2.erode(output, struc_elem)
    output = cv2.dilate(output, struc_elem)
#
cv2.imwrite('opened.png', output)


# Close (a number of times)
output = thresh.copy()
for i in range(6):
    output = cv2.dilate(output, struc_elem)
    output = cv2.erode(output, struc_elem)
#
cv2.imwrite('closed.png', output)


# Erode (a number of times) and then Dilate (a number of times)
output = thresh.copy()
for i in range(3):
    output = cv2.erode(output, struc_elem)
for i in range(3):
    output = cv2.dilate(output, struc_elem)
#
cv2.imwrite('erosions_dilations.png', output)


# Dilate (a number of times) and then Erode (a number of times)
output = thresh.copy()
for i in range(3):
    output = cv2.dilate(output, struc_elem)
for i in range(3):
    output = cv2.erode(output, struc_elem)
#
cv2.imwrite('dilations_erosions.png', output)
