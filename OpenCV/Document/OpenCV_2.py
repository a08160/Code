import cv2
import numpy as np

# 좌표 찾기
start, end = None, None

image = cv2.imread("dog.jpg")

def mouse_click(e, x, y, flag, param):
    global start, end
    if e == cv2.EVENT_LBUTTONDOWN:
        start = (x,y)
    elif e == cv2.EVENT_LBUTTONUP: # 클릭을 뗀 상태
        end = (x,y)
        # 영역 표시 ROI
        roi = image[start[1]:end[1], start[0]:end[0]]
        cv2.imshow("Select", roi)

cv2.imshow("Image", image)
cv2.setMouseCallback("Image", mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 회전 이동 (y,x) 좌표
image = cv2.imread("dog.jpg")

(h,w) = image.shape[:2]
center = (h//2,w//2) # 이미지 배열의 인덱스는 정수만 유효

matrix = cv2.getRotationMatrix2D(center, 180, 1)
rotated = cv2.warpAffine(image, matrix, (w,h))

cv2.imshow("rotate", rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 사진 이동
image = cv2.imread("dog.jpg")

matrix = np.float32([[1,0,100], [0,1,50]]) # 변환 행렬: x축으로 100pixel / y축으로 50pixel
move = cv2.warpAffine(image, matrix, (w,h))

cv2.imshow("move", move)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 실습

import cv2
import numpy as np

# 1. 이미지를 읽어서 크기를 출력하세요.
image = cv2.imread("dog.jpg")
(y, x) = image.shape[:-1]
print(f"크기: {y}x{x}")

# 2. 이미지를 흑백으로 변환하고 화면에 표시하세요.
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", image)

# 3. 이미지를 50% 크기로 축소하고 새로운 창에 표시하세요.
scale = 0.5
resized = cv2.resize(image, None, fx=scale, fy=scale)
cv2.imshow('Resized Image', resized)

# 4. 이미지를 90도 회전하여 저장하세요.
center = (x//2, y//2) 
matrix = cv2.getRotationMatrix2D(center, 90, 1)
rotated = cv2.warpAffine(image, matrix, (x, y))

# 회전된 이미지를 화면에 표시하고 저장
cv2.imshow('Rotated Image', rotated)
cv2.imwrite('rotated_dog.jpg', rotated)  # 회전된 이미지 저장

cv2.waitKey(0)
cv2.destroyAllWindows()