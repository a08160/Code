# 실습5.
# 엠보싱 / 스케치 / 카툰 효과 적용하기

import cv2 
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("practice_4.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 엠보싱 효과
array_1 = np.array([
    [-1, -1, 0], 
    [-1, 0, 1], 
    [0, 1, 1]])

embossing = cv2.filter2D(gray, -1, array_1) + 100

embossing[embossing > 255] = 255
embossing[embossing < 0] = 0
embossing = np.uint8(embossing)

plt.figure(figsize = (8,6))

plt.subplot(2, 2, 1) # Subplot: 원본 이미지
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(2, 2, 2) # Subplot: 엠보싱
plt.imshow(embossing, cmap="gray")
plt.title("Embossing (positive)")
plt.axis("off")

# 스케치 효과
inverted_gray = 255 - gray

blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

sketch = cv2.divide(gray, 255 - blurred, scale=256)

plt.subplot(2, 2, 3)
plt.imshow(sketch, cmap='gray')
plt.title("Pencil Sketch")
plt.axis("off")

# 카툰 효과
smoothed = cv2.pyrMeanShiftFiltering(image, 21, 51) # 색상 단순화화

edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)

# 카툰 효과 생성 색상과 경계를 합성
cartoon = cv2.bitwise_and(smoothed, smoothed, mask=edges)

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB))
plt.title("Cartoon Effect")
plt.axis("off")

plt.show()