import cv2

# https://github.com/kipr/opencv/tree/master/data/haarcascades

# 경로 찾기
# print(cv2.data.haarcascades)

# haar cascade xml 파일 로드
cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # haarcascade 모델 + 파일명

# 사람 이미지
image = cv2.imread("skin.webp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # OpenCV 기본. BGR => GRAY

# 얼굴 탐지
# scaledFactor: 이미지의 크기를 줄여가면서 객체를 찾는 비율
# minNeighbors: 객체로 인정하기 위한 최소의 사각형 개수(ROI의 이웃)
# minSize: 감지할 최소 객체 크기(너무 작은 객체는 무시)
# maxSize: 감지할 최대 객체 크기(너무 큰 객체는 무시)
# detectMultiScale() 메서드의 반환값 (x, y, width, height)
faces = cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (10,10))

# 탐지된 얼굴에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("face", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 눈 탐지
import cv2

# 얼굴 탐지 모델 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 눈 탐지 모델 로드
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# 이미지 로드 및 그레이스케일 변환
image = cv2.imread("skin.webp")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 얼굴 탐지
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴에 사각형 그리기
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # 얼굴 영역을 ROI로 설정
    face_roi = gray[y:y + h, x:x + w]
    face_color_roi = image[y:y + h, x:x + w]

    # 눈 탐지
    eyes = eye_cascade.detectMultiScale(face_roi, scaleFactor=1.01, minNeighbors=1, minSize=(0,0))

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_color_roi, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)

# 결과 출력
cv2.imshow("Detected Eyes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
