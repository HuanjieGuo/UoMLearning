# snippet_07.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Create and display an image histogram using matplotlib.
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

# Calculate the histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = hist.reshape(256)

# Plot histogram
plt.bar(np.linspace(0,255,256), hist)
plt.title('Histogram')
plt.ylabel('Frequency')
plt.xlabel('Grey Level')
plt.show()
