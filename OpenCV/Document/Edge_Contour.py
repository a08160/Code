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


# Coutour
# 이진화 처리
_, thresh = cv2.threshold(canny, 127, 25, cv2.THRESH_BINARY)

# 컨투어 감지
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 컨투어 원본에 그리기
result_image = image.copy()
cv2.drawContours(result_image, contours, 0, -1, [0,255,0], 2)

plt.subplot(2,2,3)
plt.imshow(cv2.cvtColor(result_image),cv2.COLOR_GRAY2BGR)
plt.title("contour")
plt.axis("off")

plt.show()

# 컨투어 계산
for i in contours:
    # 면적 계산
    print(f"면적: {cv2.contourArea(contours)}")

    # 중심점 계선
    M = cv2.moments(contours)
    if M['m00'] != 0: # 중심점 계산(m00 면적)
        cx = int(M['m10']/M['m00']) # m: moment 값 m10: x에 대한 1차 모멘트 값
        cy = int(M['m01']/M['m00'])
        print(f"Centroid: {({cx}, {cy})}")

        # 중심점 표시
        cv2.circle(image, (cx,cy), 5, (0,0,225), -1)
    
    # 둘레 계산
    perimeter = cv2.arcLength(contours, True) # Trye = 폐곡선 여부
    print(f"Arc Length: {perimeter}")

    # 컨투어 그리기
    cv2.drawContours(image, [contours], -1, (0,255,0),2) # 초록색 윤곽선