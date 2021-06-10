# snippet_20.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Access a webcam and display the video stream.
"""

import cv2


# Get hold of the first video camera on the computer
cap = cv2.VideoCapture(0)

# Loop forever (until Escape pressed)
while(True):
    # Capture frame from the camera
    ret, frame = cap.read()

    # Our operations on the frame come here
    channels = cv2.split(frame)
    # Swap channels around
    channelsOut = [channels[1], channels[2], channels[0]]
    output = cv2.merge(channelsOut)

    # Display the resulting frame
    cv2.imshow('frame', output)

    # Wait for Escape press before closing,
    # otherwise window will close without you seeing it
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
