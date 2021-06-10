# snippet_11.py
# -----------------------

"""
Python Code Snippets
Terence Morley, Department of Computer Science,
    The University of Manchester, Nov 2020

Purpose: Add noise to an image.
"""

import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np


input_file = 'retina.png'
img = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
#
# Check for success
if img is None:
    print('Failed to open', input_file)
    sys.exit()


# Add Gaussian noise
imgSign = img.astype(np.int16) # convert image to signed integer
imnoise = np.zeros(img.shape, np.int16) # Blank image for noise
#
mean = 0
sigma = 40
cv2.randn(imnoise, mean, sigma) # create the random distribution
#
noisy_img = cv2.add(imgSign, imnoise) # add the noise to the original image
cv2.imwrite('gaussian_noise.png', noisy_img)


# Add Salt and Pepper noise
noise_prob = 0.01
noise = np.random.binomial(1, noise_prob, img.shape[0]*img.shape[1]) * 255
salt = noise.reshape(img.shape)
noise = np.random.binomial(1, noise_prob, img.shape[0]*img.shape[1]) * 255
pepper = noise.reshape(img.shape)
#
noisy_img = np.where(salt, 255, img)
noisy_img = np.where(pepper, 0, noisy_img)
cv2.imwrite('salt_n_pepper.png', noisy_img)
