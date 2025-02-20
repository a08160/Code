from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt") # YOLO모델 v8, n: nano버전

image = cv2.imread("YOLO_test.webp")

# 객체 탐지 
# 반환값은 탐지 결과의 리스트 형태. results[0]: 이미지에 대한 결과
results = model.predict(source = image,
              save=False,
              save_txt = False, 
              conf=0.5 # conf: 신뢰도 임계값(Threshold)
              )

# 결과 시각화
frame = results[0].plot()

# plot(): 탐지된 객체를 시각화한 이미지를 반환

# 창 크기 조절 가능하도록 설정
cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)

# 창 크기 설정 (가로 800px, 세로 600px)
cv2.resizeWindow("YOLO", 800, 600)

cv2.imshow('YOLO', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 웹캠 구현
# 웹캠 열기
cap = cv2.VideoCapture(0)

# 저장을 위한 설정 (FPS, 해상도, 코덱)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20.0
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# 영상 저장 객체 생성
out_original = cv2.VideoWriter('YOLO.avi', fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # 웹캠 종료 시 루프 탈출

    # 객체 탐지
    results = model.predict(source=frame, save=False, conf=0.5)

    # 결과 시각화
    frame = results[0].plot()

    # 영상 저장
    out_original.write(frame)

    # 창 크기 조절 가능하도록 설정
    cv2.namedWindow("YOLO", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("YOLO", 800, 600)

    # 화면 출력
    cv2.imshow('YOLO', frame)

    # 'q'를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
out_original.release()
cv2.destroyAllWindows()
