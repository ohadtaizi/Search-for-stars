import cv2
import numpy as np
import matplotlib.pyplot as plt

import os
def images_paths():
    # image_paths = []
    image_dir = r'C:Users\Ohad\PycharmProjects\pythonProject'
    if not os.path.isdir(image_dir):
        print('Directory not found:', image_dir)

    # List to store image file paths

    # Traverse the directory tree and find all image files
    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith(('.jpg', '.jpeg', '.png')):
                image_paths.append(os.path.join(root, file))

    # Print the list of image
    print(image_paths)


def print_hi():

    img = cv2.imread(r'C:\Users\Ohad\PycharmProjects\pythonProject\WhatsApp Image 2023-04-03 at 09.46.44.jpeg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    nummber_stars = len(contours)
    print(nummber_stars)
    plt.imshow(img)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
     # print_hi()
    images_paths()
