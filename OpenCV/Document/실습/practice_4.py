# 실습4.
# 마우스를 움직이면 해당 위치 주변이 확대되는 돋보기 효과를 적용하세요.

import cv2
import numpy as np

# 이미지 읽어오기
img = cv2.imread('practice_3.jpg')
image = cv2.resize(img, (800, 600))

zoom_factor = 1.0
zoom_step = 0.1
window_name = 'Magnifier'

def zoom(event, x, y, flags, param):
    global zoom_factor

    if event == cv2.EVENT_MOUSEWHEEL:
        if flags > 0:
            zoom_factor += zoom_step
        else:
            zoom_factor -= zoom_step

        zoom_factor = max(1.0, zoom_factor)  # 최소 배율 제한

    elif event == cv2.EVENT_MOUSEMOVE:
        # 확대된 이미지 생성
        h, w, _ = image.shape
        zoomed_image = cv2.resize(image, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)

        # 마우스 위치 중심으로 확대된 이미지에서 영역 선택
        zoom_h, zoom_w, _ = zoomed_image.shape
        cx, cy = int(x * zoom_factor), int(y * zoom_factor)

        # 확대된 이미지에서 적절한 부분 선택
        sx = max(0, min(zoom_w - w, cx - w // 2))
        sy = max(0, min(zoom_h - h, cy - h // 2))
        ex, ey = sx + w, sy + h

        cropped = zoomed_image[sy:ey, sx:ex]

        # 원본 크기로 맞추기
        result = np.zeros_like(image)
        result[:cropped.shape[0], :cropped.shape[1]] = cropped

        cv2.imshow(window_name, result)

cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, zoom)
cv2.imshow(window_name, image)

while True:
    if cv2.waitKey(1) == 27:  # Esc 키로 종료
        break

cv2.destroyAllWindows()

