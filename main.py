import matplotlib as matplotlib
import pytesseract
import shutil
import os
import random
try:
    from PIL import Image
except ImportError:
    import Image

import matplotlib.pyplot as plt
import cv2

img = cv2.imread("/Users/jackhamilton/PycharmProjects/test/venv/pictures/TEST_9999.jpg")
print(type(img))
print(img.shape)

img = cv2.bitwise_not(img)
plt.imshow(img)
