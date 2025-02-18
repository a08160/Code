import cv2
import numpy as np

# 좌표 찾기
def mouse_click(e, x, y, flag, param):
    if e == cv2.EVENT_LBUTTONDOWN:
        print(f"마우스 위치 : x={x}, y={y}")

image = cv2.imread("dog.jpg")

cv2.imshow("Image", image)
cv2.setMouseCallback("Image", mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()