# snippet_15.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Write your own functions and draw on an image.
"""

import cv2
import sys
import numpy as np


#############################################################
## myInvert()
##
def myInvert(imIn):
    # create a new image that is the negative of the original
    imOut = 255 - imIn

    return imOut
#############################################################




#############################################################
## myInvert()
##
def makeDrawing():
    # Create a new image with pixels set to 0 (black)
    # height=200, width=400. That is Rows, Columns (Rhubarb and Custard)
    # ** BUT SEE BELOW: OpenCV is (x,y) not (r,c)
    # The 3 is the number of channels: BGR
    imOut = np.zeros((200,400,3), np.uint8)

    # Outline of red square. OpenCV coordinates are ordered (x,y)
    imOut = cv2.rectangle(imOut, (50, 50), (100,100), (0, 0, 255) )

    # Thicker outline of red square
    imOut = cv2.rectangle(imOut, (60, 60), (90,90), (0, 0, 255), 4 )

    # Solid blue square (negative width values cause it to be filled)
    imOut = cv2.rectangle(imOut, (200, 50), (250,100), (255, 0, 0), -1 )

    # Yellow circle
    imOut = cv2.circle(imOut, (225, 75), 100, (0, 255, 255) )

    # Green solid ellips (second parameter is type RotatedRect)
    # RotatedRect is ( (centre point), (rectange size), rotation angle )
    imOut = cv2.ellipse(imOut, ((300, 150), (100, 50), 45), (0, 255, 0), -1 )

    # Draw some text
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = cv2.putText(imOut, 'Hello there.', (20,40), font, 2, (255,255,255), 2, cv2.LINE_AA)

    return imOut
#############################################################




#############################################################
## The main 'function'
##
if __name__ == '__main__':
    input_file = 'xray.jpg'
    img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
    #
    # Check for success
    if img is None:
        print('Failed to open', input_file)
        sys.exit()

    # Call your image invert function
    inverted = myInvert(img)
    cv2.imwrite('xray_invert.jpg', inverted)

    # Call your function that returns a new image
    drawing = makeDrawing()
    cv2.imwrite('drawing.jpg', drawing)
#############################################################
