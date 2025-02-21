import cv2
import numpy as np

# 얼굴과 입을 감지할 캐스케이드 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# 이미지 로드
image = cv2.imread("practice_2.jpg")
image = cv2.resize(image, (600, 600))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(50, 50))

for (x, y, w, h) in faces:

    # 얼굴 영역에 대해 입 검출
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    
    # 입 검출 (얼굴 영역 내에서)
    mouths = mouth_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))
    
    for (mx, my, mw, mh) in mouths:
        # 입 영역을 잘라내기
        mouth_region = roi_color[my:my+mh, mx:mx+mw]
        
        # 모자이크 효과 (작게 축소 후 다시 확대)
        small = cv2.resize(mouth_region, (8, 8), interpolation=cv2.INTER_NEAREST)
        mosaic = cv2.resize(small, (mw, mh), interpolation=cv2.INTER_NEAREST)
        
        # 원본 이미지에 모자이크된 입 영역 반영
        roi_color[my:my+mh, mx:mx+mw] = mosaic

# 결과 이미지 시각화 (얼굴 영역에 빨간색 사각형이 그려짐)
cv2.imshow("Mosaic Effect with Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
