# snippet_08.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Access pixels and regions (slicing).
"""

import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np


input_file = 'balloons.jpg'
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()

# Access a rectangle of pixels individually
print('\nAccess pixels individually:')
for row in range(100,105):
    for col in range(150,155):
        print(img[row, col], ' ', end='')
    print()

# Access a rectangle of pixels with slicing
print('\nAccess pixels with slicing:')
region = img[100:105, 150:155]
print(region)

# Note that the pixel accesses return references to pixels
# Look at the original image when the region is changed
print('\nSetting slice to zero:')
for row in range(region.shape[0]):
    for col in range(region.shape[1]):
        region[row, col] = 0
print("Region:\n", region)
print("The part of original image:\n", img[100:105, 150:155])

# Make a copy of the slice to change it without changing the original
print('\nSetting COPY of slice to 128:')
region = img[100:105, 150:155].copy()
for row in range(region.shape[0]):
    for col in range(region.shape[1]):
        region[row, col] = 128
print("Region:\n", region)
print("The part of original image:\n", img[100:105, 150:155])
