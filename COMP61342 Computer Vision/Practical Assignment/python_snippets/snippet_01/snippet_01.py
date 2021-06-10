# snippet_01.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Load an image, save it in a different format and display it.
"""

import cv2

# Open JPEG image
img = cv2.imread('earth.jpg')

# Display image
cv2.namedWindow('Source Image')
cv2.imshow('Source Image', img)

# Save image in PNG format
cv2.imwrite('earth.png', img)

# Wait for spacebar press before closing,
# otherwise window will close without you seeing it
while True:
    if cv2.waitKey(1) == ord(' '):
        break

cv2.destroyAllWindows()
