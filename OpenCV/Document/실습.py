import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 저장을 위한 설정 (FPS, 해상도, 코덱)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# 영상 저장 객체 생성
out_original = cv2.VideoWriter('original.avi', fourcc, fps, (frame_width, frame_height))
out_contours = cv2.VideoWriter('contours.avi', fourcc, fps, (frame_width, frame_height))
out_sharpened = cv2.VideoWriter('sharpened.avi', fourcc, fps, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 1. 그레이스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. 임계값 처리 (이진화)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # 3. 컨투어 탐지
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 컨투어 그리기 (윤곽선 감지 영상용)
    contour_img = frame.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

    # 4. 샤프닝 필터 적용
    sharpening_kernel = np.array([[0, -1, 0],
                                  [-1, 5, -1],
                                  [0, -1, 0]])
    sharpened = cv2.filter2D(frame, -1, sharpening_kernel)

    # 5. 영상 저장
    out_original.write(frame)
    out_contours.write(contour_img)
    out_sharpened.write(sharpened)

    # 6. 영상 표시
    cv2.imshow('Original', frame)
    cv2.imshow('Contours Detected', contour_img)
    cv2.imshow('Sharpened', sharpened)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
out_original.release()
out_contours.release()
out_sharpened.release()
cv2.destroyAllWindows()
