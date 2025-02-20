import cv2
import numpy as np
import matplotlib.pyplot as plt

# 색상 필터링. 이미지 영역에서 초록색
image = cv2.imread("hsv_image.png")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # BGR 이미지를 HSV로 변환

# 색상 범위 정의 (초록색)
lower = np.array([28, 70, 70])  # 초록색 범위의 하한
upper = np.array([85, 255, 255])  # 초록색 범위의 상한

mask = cv2.inRange(hsv_image, lower, upper) # mask 생성

# 윤곽선 검출
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
for contour in contours:
    if cv2.contourArea(contour) > 500:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

resized_image = cv2.resize(image, (600, 400))  # 이미지 크기 조정

# 결과 시각화
cv2.imshow("Filter", resized_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 물체 개수
num = list(filter(lambda x: cv2.contourArea(x) > 500, contours))
print(f"검출된 초록색 물체의 개수: {len(num)}개")
