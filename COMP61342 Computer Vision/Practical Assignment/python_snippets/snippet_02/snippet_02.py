# snippet_02.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Load an image, check that it loaded successfully and
    save it in greyscale.
"""

import cv2
import sys

# Open image
filename = 'earth.jpg'
img = cv2.imread(filename)

# Check for success
if img is None:
    print('Error: failed to open', filename)
    sys.exit()

# Convert to greyscale and save it
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('earth_grey.jpg', grey)
