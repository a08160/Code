import cv2
import numpy as np

image = cv2.imread('dog.jpg')
cv2.imshow('Color Image', image)

gray_image = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE) # 회색 배경 제시시
cv2.imshow('Gray Image',gray_image)

cv2.waitKey(2000) # waitkey(delay) 창을 무한 대기 / 1초 = 1000

key = cv2.waitKey(2000)
if key == ord("o"): # 아스키 코드로 변환
    print(chr(key)) # 문자로 변환

# 창 닫기
cv2.destroyAllWindows() # 모든 창을 닫음
# cv2.destroyWindows(창이름) 지정 창 닫음음

# 도형 그리기
width = 500
height = 500
canvas = np.zeros((height,width,3), dtype=np.uint8) # 3: 컬러채널 1: 흑백채널널

# 직선 그리기(그릴 캔버스, 시작점, 끝점, 색상, 두께)
cv2.line(canvas, (50,50),(450,50), (0,255,0), 3)

cv2.rectangle(canvas, (50,100), (200,250),(0,0,255), 2) # 색상 컬러는 BGR 순서

# 원 그리기(그릴 캔서브, 중심 좌표, 반지름, 색상, 두께)
cv2.circle(canvas, (300, 200), 50, (255,0,0), 3) # 두께 = -1 내부 채우기

# 다각형 그리기 - 그리기 위한 점 포인트가 필요
pts = np.array([[250,300],[50,250],[30,33],[100,100]])
pts = pts.reshape([-1,1,2]) # -1 : 자동 계산
cv2.polylines(canvas, [pts], isClosed = True,color = (255,255,0), thickness = 2)

# 텍스트 추가
cv2.putText(canvas, "hello OpenCV", (128,450), cv2.FONT_HERSHEY_COMPLEX,
             1, # 글자 크기
             (255,255,255), # 색상
             2
) # 두께

cv2.imshow("Canvas", canvas)
cv2.waitKey(2000)
cv2.destroyAllWindows()


# 이미지 색상 변경
image = cv2.imread("dog.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # hsv 색을 직관적으로 제시하여 색 추출에서 쉬움움

scale = 0.5
resized = cv2.resize(image, None, fx = scale, fy = scale)
# resized = cv2.resize(image, (50,50))

# 이미지 저장
cv2.imwrite('Dog_resized.jpg', resized)

# ROI (y,x) 값으로 좌표값을 반영
roi = image[50:200, 30:100].copy()

cv2.imshow("Roi", roi)
cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()