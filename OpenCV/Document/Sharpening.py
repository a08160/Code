# 샤프닝

import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread("dog.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
blurred = cv2.medianBlur(image_rgb,5)

kernel = np.array([[0,-1,0],
                   [-1,5,-1],
                   [0,-1,0]])

# 필터 적용
sharped = cv2.filter2D(blurred, -1 ,kernel)

plt.imshow(sharped)
plt.axis("off")
plt.show()