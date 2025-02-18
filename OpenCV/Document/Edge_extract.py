# 엣지 추출

import matplotlib.pyplot as plt
import cv2
import numpy as np

image = cv2.imread("dog.jpg", cv2.IMREAD_GRAYSCALE)

# Sobel 필터 x,y 방향 미분
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3) # 정밀도를 높이기 위해 부동 소수점 사용
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x,sobel_y)

plt.figure(figsize= (10,10))
plt.subplot(2,2,1)
plt.imshow(image, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(2,2,2)
plt.imshow(sobel_combined, cmap="gray")
plt.title("sobel")
plt.axis("off")

# Laplacian
laplacian = cv2.Laplacian(image, cv2.CV_64F)
plt.subplot(2,2,3)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian")
plt.axis("off")

# canny
canny = cv2.Canny(image, 100,100)
plt.subplot(2,2,4)
plt.imshow(sobel_combined, cmap="gray")
plt.title("Canny")
plt.axis("off")

plt.show()