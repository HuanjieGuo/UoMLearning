import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('birds.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Display image
plt.figure()
plt.imshow(img)

plt.figure()
imgGrey =  cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imwrite('sky_grey.jpg', imgGrey)

# get the bird 76
thres = 76
_, bird = cv2.threshold(imgGrey, thres, 255, cv2.THRESH_BINARY)
plt.figure()
cv2.imwrite('bird_grey.jpg', bird)

# open

# # Create structuring element
# struc_elem = cv2.getStructuringElement(cv2.MORPH_OPEN, (2,2))
# for i in range(5):
#     bird = cv2.erode(bird, struc_elem)
#     bird = cv2.dilate(bird, struc_elem)

# labeling
birds_list = []
bird_img = bird.copy()
one_bird_pixel = []
height, width = bird_img.shape

def dfs(raw, col):
    if not (raw>=0 and raw<height and col>=0 and col<width):
        return
    if bird_img[raw][col] == 0:
        one_bird_pixel.append([raw, col])
        bird_img[raw][col] = 255
    else:
        return
    dfs(raw - 1, col)
    dfs(raw + 1, col)
    dfs(raw, col - 1)
    dfs(raw, col + 1)
    dfs(raw - 1, col - 1)
    dfs(raw + 1, col-1)
    dfs(raw - 1, col + 1)
    dfs(raw + 1, col + 1)

for raw in range(0, height):
    for col in range(0, width):
        dfs(raw, col)
        if (len(one_bird_pixel) >= 10):
            birds_list.append(one_bird_pixel.copy())
        one_bird_pixel = []

import random

def black_sky_color_bird():
    black_img = np.zeros([height,width,3])
    for bird_idx in birds_list:
        # get random color (492, 800, 3)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        for point in bird_idx:
            black_img[point[0]][point[1]][0] = r
            black_img[point[0]][point[1]][1] = g
            black_img[point[0]][point[1]][2] = b
    cv2.imwrite("color_birds_black_sky.jpg",black_img)
    #cv2.imwrite("open_color_birds_black_sky.jpg",black_img)

def color_sky_color_bird():
    new_img = img.copy()
    print(len(birds_list))
    for bird_idx in birds_list:
        # get random color (492, 800, 3)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        for point in bird_idx:
            new_img[point[0]][point[1]][0] = r
            new_img[point[0]][point[1]][1] = g
            new_img[point[0]][point[1]][2] = b

    cv2.imwrite("color_birds_sky.jpg",cv2.cvtColor(new_img,cv2.COLOR_RGB2BGR))

if __name__ == '__main__':
    black_sky_color_bird()
    color_sky_color_bird()