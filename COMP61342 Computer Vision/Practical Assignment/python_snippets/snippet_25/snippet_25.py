# snippet_25.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Image segmentation with Mean-Shift.

Sources
-------
Python Wrapper: Frederic Jean, https://github.com/fjean/pymeanshift
C++ library: Chris M. Christoudias, Bogdan Georgescu
Algorithm design:
    D. Comaniciu, P. Meer: Mean Shift: A robust approach toward feature space analysis.
    C. Christoudias, B. Georgescu, P. Meer: Synergism in low level vision.
 """

import cv2
import pymeanshift as pms
# pymeanshift library was obtained from https://github.com/fjean/pymeanshift
# It has been built on Fedora Linux and is placed in the folder with this script.
# It can be installed into Python if necessary (see the included zip file)
#
# If the supplied libraries do not work on your computer, instructions for compiling
# the library are given at the bottom of this file and also in the readme files in the zip.


###############################################################
##
if __name__ == '__main__':

    # ------------------- Image 1 ---------------------
    # Open image
    filename = 'pavement.png'
    img = cv2.imread(filename)

    # Check for success
    if img is None:
        print('Error: failed to open', filename)
        sys.exit()

    # Perform mean-shift segmentation
    (segmented_image, labels_image, number_regions) = pms.segment(img, spatial_radius=5,
                                                                  range_radius=4.5, min_density=50)

    cv2.imwrite('pavement_meanshift.png', segmented_image)


    # ------------------- Image 2 ---------------------
    filename = 'beach.jpg'
    img = cv2.imread(filename)

    # Check for success
    if img is None:
        print('Error: failed to open', filename)
        sys.exit()

    # Perform mean-shift segmentation
    (segmented_image, labels_image, number_regions) = pms.segment(img, spatial_radius=5,
                                                                  range_radius=4.5, min_density=50)

    cv2.imwrite('beach_meanshift.png', segmented_image)


##############################################
"""
Instructions for compiling the mean-shift library
--------------------------------------------------
0. Install python development libraries:
    sudo apt-get install python3-dev
1. Unzip pymeanshift-master.zip
2. Open a terminal in the pymeanshift-master directory
3. Type:
    python3 setup.py build
4. Copy the two files from /pymeanshift-master/build/lib.linux-x86_64-3.8 into the
    same directory as your Python script that uses the mean-shift library.
"""
