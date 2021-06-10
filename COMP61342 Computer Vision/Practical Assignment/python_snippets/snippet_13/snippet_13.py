# snippet_13.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Find lines and circles in an image with the Hough Transform.
"""

import cv2
import sys
import numpy as np

# ---------------------- Hough lines -----------------------
input_file = 'building.jpg'
img = cv2.imread(input_file)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()


# Canny edge detector
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
edges = cv2.Canny(grey, 200, 230, 2)
cv2.imwrite('edges_for_lines.png', edges)

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, 60, 10)
print('Found {} lines'.format(len(lines)))
#
for i in range(len(lines)):
    x1, y1, x2, y2 = lines[i][0]
    img = cv2.line(img, (x1, y1), (x2, y2), (255,0,0), 3)
cv2.imwrite('hough_lines.png', img)



# ---------------------- Hough circles -----------------------
input_file = 'coins.jpg'
img = cv2.imread(input_file)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()


# Canny edge detector
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
grey = cv2.medianBlur(grey, 5)
edges = cv2.Canny(grey, 150, 230, 2)
cv2.imwrite('edges_for_circles.png', edges)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 100, param1=60,param2=30,minRadius=10,maxRadius=100)
circles = circles[0].astype(np.uint16)
print('Found {} circles'.format(len(circles)))
#
for i in range(len(circles)):
    x, y, r = circles[i]
    img = cv2.circle(img, (x, y), r, (255,0,0), 3)
cv2.imwrite('hough_circles.png', img)
