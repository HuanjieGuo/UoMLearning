# snippet_21.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Read and write a video file.
"""

import cv2
import sys


# Get the video file
video = cv2.VideoCapture('../data/ball.avi')
#
if not video.isOpened():
    print("Error reading video file.")
    sys.exit()


# Get details of video
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(video.get(cv2.CAP_PROP_FPS))


# Make a video file for the output
videoOutput = cv2.VideoWriter('ball_slow.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'), int(fps/2), (width, height))


# Loop forever (until Escape pressed)
while(True):
    # Capture frame from the camera
    ret, frame = video.read()
    if frame is None:
        break

    # Write frame to video file
    videoOutput.write(frame)
