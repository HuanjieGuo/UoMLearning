# snippet_10.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Filtering a greyscale image.
"""

import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np


input_file = 'retina.png'
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()


# Gaussian blurring
output = cv2.GaussianBlur(img, (0,0), 3)
cv2.imwrite('gaussian_sd3.jpg', output)
#
output = cv2.GaussianBlur(img, (0,0), 6)
cv2.imwrite('gaussian_sd6.jpg', output)


# Sobel edge detection (combine horiz. and vert. edges)
grad_x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
grad_y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
#
abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)
grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
#
output = grad.astype(np.uint8)
cv2.imwrite('sobel.jpg', output)


# Laplacian
output = cv2.Laplacian(img, cv2.CV_16S)
output = cv2.convertScaleAbs(output)
output = np.interp(output, (output.min(), output.max()), (0, 255))
output = output.astype(np.uint8)
cv2.imwrite('laplacian.jpg', output)


# User-defined kernel
kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]) / 1
output = cv2.filter2D(img, cv2.CV_8U, kernel)
cv2.imwrite('user_defined.jpg', output)


# Open image that has salt and pepper noise
input_file = 'salt_n_pepper.png'
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()

# Median filter
output = cv2.medianBlur(img, 3)
cv2.imwrite('median.jpg', output)
