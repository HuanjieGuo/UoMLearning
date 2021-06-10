# snippet_04.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Load an image as greyscale and perform inversion
    and brightness and contrast adjustments.
"""

import cv2
import sys
import numpy as np


# Open image
filename = 'earth.jpg'
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# Check for success
if img is None:
    print('Error: failed to open', filename)
    sys.exit()

# Save greyscale image
cv2.imwrite('earth_grey.jpg', img)

# Invert - Image Negative
output = 255 - img
cv2.imwrite('earth_invert.jpg', output)

# Convert image to integer type so if values go outside
# the range 0-255, we can clip it
img = img.astype(np.int)

# Increase brightness
output = img + 50
output = np.clip(output, 0, 255)
cv2.imwrite('earth_brighter.jpg', output)

# Decrease brightness
output = img - 50
output = np.clip(output, 0, 255)
cv2.imwrite('earth_darker.jpg', output)

# Increase contrast
output = img * 2
output = np.clip(output, 0, 255)
cv2.imwrite('earth_contrast_hi.jpg', output)

# Decrease contrast
output = img * 0.5
output = np.clip(output, 0, 255)
cv2.imwrite('earth_contrast_lo.jpg', output)
