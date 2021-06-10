# snippet_22.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Very basic motion tracking.
"""

import cv2
import numpy as np
import sys

#########################################
##
def getCentreOfMass(img):
    rSum = 0
    cSum = 0
    pxCount = 0

    # NOTE: Accessing individual pixels in Python is very slow,
    # especially when we are doing it for many frames.
    # It is possible to write a C library to access the image data
    # and call it from Python.

    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            if img[r,c] == 255:
                rSum += r
                cSum += c
                pxCount += 1

    pt = (0,0)
    if pxCount > 0:
        pt = (int(cSum/pxCount), int(rSum/pxCount))

    return pt
#########################################



# Get the video file
video = cv2.VideoCapture('../data/ball_slow.avi')
#
if not video.isOpened():
    print("Error reading video file.")
    sys.exit()

print('NOTE: this will take a minute or so.')

# Get details of video
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))


# Make a video file for the output
videoOutput = cv2.VideoWriter('ball_motion.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'), int(fps/2), (width, height))


lastFrame = None

# Loop forever (until Escape pressed)
while(True):
    # Capture frame from the camera
    ret, frame = video.read()
    if frame is None:
        break

    # Blur the frame and convert it to int (so we can do signed maths)
    currentFrame = cv2.GaussianBlur(frame, (0,0), 2) # PARAMETER TO CHANGE FOR OTHER VIDEOS
    currentFrame = cv2.cvtColor(currentFrame, cv2.COLOR_BGR2GRAY).astype(np.int)

    # Don't do anything with the first frame
    if lastFrame is None:
        lastFrame = currentFrame
        continue

    # Find the difference of this frame and the last to see what has changed.
    output = abs(currentFrame - lastFrame).astype(np.uint8)
    _, output = cv2.threshold(output, 24, 255, cv2.THRESH_BINARY) # PARAMETER TO CHANGE FOR OTHER VIDEOS

    # White is where the movement is
    cog = getCentreOfMass(output)
    output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

    # Draw a circle on the original frame showing where we have detected movement
    frame = cv2.circle(frame, cog, 20, (0,0,255), -1)

    # Write frame to video file (to see the difference video, write 'output' to the video file)
    videoOutput.write(frame)

    # Save current frame
    lastFrame = currentFrame
