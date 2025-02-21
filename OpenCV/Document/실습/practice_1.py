import cv2
import matplotlib.pyplot as plt
import numpy as np

# 이미지 읽기
image = cv2.imread("practice_1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 가우시안 블러로 노이즈 감소
blurred = cv2.medianBlur(gray, 5)

# 캐니 엣지 검출
canny = cv2.Canny(blurred, 50, 200)

# 원 검출
rows = canny.shape[0]
circles = cv2.HoughCircles(canny, cv2.HOUGH_GRADIENT, 1, rows/8,
                           param1=100, param2=30,
                           minRadius=15, maxRadius=50)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        radius = i[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)  # 원의 중심과 경계 그리기

# 사각형 검출
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    aa = cv2.approxPolyDP(contour, 0.03*cv2.arcLength(contour, True), True)
    if len(aa) == 4 and cv2.contourArea(contour) >= 30:  # 면적 30 이상으로 필터링
        cv2.drawContours(image, [aa], 0, (0,0,255), 2)  # 사각형 그리기

# Sharpening 필터 적용
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])  # 기본 sharpening 커널
sharpened = cv2.filter2D(image, -1, kernel)

# 이미지 크기 조정
resized = cv2.resize(sharpened, (600,600))

# 결과 시각화
image_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)  # OpenCV -> Matplotlib 색상 변환
plt.figure(figsize=(8, 8))
plt.imshow(image_rgb)
plt.axis("off")
plt.show()
