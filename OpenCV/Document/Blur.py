import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("dog.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# matplotlib으로 이미지 표시하기
# matplotlib은 무조건 RGB로 표기
plt.figure(figsize = (12,12))
plt.subplot(2,2,1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis("off") # 눈금 삭제

# 이미지 전처리(이미지 필터링 및 노이즈 제거)
# 평균 블러링
blurred = cv2.blur(image_rgb, (5,5))
plt.subplot(2,2,2)
plt.imshow(blurred)
plt.title("Blur")
plt.axis("off") # 눈금 삭제

# 가우시안 블러링
blurred = cv2.GaussianBlur(image_rgb,(5,5), 0) # x방향 표준편차: 0 대입 시 자동 계산
plt.subplot(2,2,3)
plt.imshow(blurred)
plt.title("GaussianBlur")
plt.axis("off") # 눈금 삭제

# 미디안 블러링
blurred = cv2.medianBlur(image_rgb,5)
plt.subplot(2,2,4)
plt.imshow(blurred)
plt.title("MedianBlur")
plt.axis("off") # 눈금 삭제

plt.show()