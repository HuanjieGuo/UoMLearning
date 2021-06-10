# snippet_23.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Face detection with Viola-Jones.

Source: https://www.datacamp.com/community/tutorials/face-detection-python-opencv

Haar classifiers can be found in your OpenCV directory: opencv/data/haarcascades/
"""

import numpy as np
import cv2


# ================================================
#
def detectFaces(filename):
    # Open image
    img = cv2.imread(filename)

    # Check for success
    if img is None:
        print('Error: failed to open', filename)
        sys.exit()

    # Classifier works on greyscale images
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create classifier.
    # More Haar classifiers can be found in your OpenCV directory:
    # opencv/data/haarcascades/
    haar_cascade_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Detect faces
    faces_rects = haar_cascade_face.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 5);

    # Print out number of faces found
    print('Number of faces found: ', len(faces_rects))

    # Draw a rectangle around each detected face
    output = img.copy()
    for (x,y,w,h) in faces_rects:
         cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return output
# ================================================



# ================================================
#
if __name__ == '__main__':

    # ---------------- Image 1 -------------------
    # Detect faces in specified image file
    out = detectFaces('baby.png')

    # Save image with detected face
    outFilename = 'baby_detected_faces.png'
    print('Saving to {}'.format(outFilename))
    cv2.imwrite(outFilename, out)

    # Show results
    cv2.namedWindow('Display')
    cv2.imshow('Display', out)

    # Wait for spacebar press or escape before closing,
    # otherwise window will close without you seeing it
    while True:
        key = cv2.waitKey(1)
        if key == ord(' ') or key == 27:
            break

    cv2.destroyAllWindows()


    # ---------------- Image 2 -------------------
    # Detect faces in specified image file
    out = detectFaces('small_crowd.png')

    # Save image with detected face
    outFilename = 'small_crowd_detected_faces.png'
    print('Saving to {}'.format(outFilename))
    cv2.imwrite(outFilename, out)
