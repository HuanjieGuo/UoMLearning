# snippet_03.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Load a colour image and save the three colour channels.
"""

import cv2
import sys

# Open image
filename = 'balloons.jpg'
img = cv2.imread(filename)

# Check for success
if img is None:
    print('Error: failed to open', filename)
    sys.exit()

# Split into Blue, Green and Red channels and save them.
# NOTE The default format in OpenCV is BGR not RGB.
blue, green, red = cv2.split(img)
cv2.imwrite('balloons_blue.jpg', blue)
cv2.imwrite('balloons_green.jpg', green)
cv2.imwrite('balloons_red.jpg', red)

# Alternative method - Array
channels = cv2.split(img)
cv2.imwrite('balloons_green2.jpg', channels[1])
