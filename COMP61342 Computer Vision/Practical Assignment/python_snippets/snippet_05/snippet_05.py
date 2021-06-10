# snippet_04.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Change image brightness with a TrackBar (or slider).
"""

import cv2
import sys

# ================================================
# Callback function to receive messages from the TrackBar
def change(x):
    # Change brightess by adding a value to every pixel.
    # That is, the value sent from the TrackBar
    output = img + x
    cv2.imshow('Display - Note overflow', output)

    # Notice that if the brightness value is too large, the
    # pixel value will wrap around. This method won't clip it.
# ================================================



# ================================================
if __name__ == "__main__":
    # Open image
    filename = 'dark_street.jpg'
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # Check for success
    if img is None:
        print('Error: failed to open', filename)
        sys.exit()

    # Create a window to display the image in
    cv2.namedWindow('Display - Note overflow', cv2.WINDOW_NORMAL)
    cv2.imshow('Display - Note overflow', img) # Show initial image

    # Create TrackBar
    cv2.createTrackbar('Brightness', 'Display - Note overflow', 0, 50, change)

    # Wait for spacebar press before closing,
    # otherwise window will close without you seeing it
    while True:
        if cv2.waitKey(1) == ord(' '):
            break

    cv2.destroyAllWindows()
