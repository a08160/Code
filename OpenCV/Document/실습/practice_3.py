import cv2

# 이미지 로드
image = cv2.imread("practice_3.jpg")
image = cv2.resize(image, (800, 600))

# 드로잉 상태 및 시작점 초기화
drawing = False
start_point = (-1, -1)
mode = "circle"  # 기본적으로 원 모드로 설정

# 드로잉 함수
def draw(event, x, y, flags, param):
    global drawing, start_point, image, temp_image, mode

    # 드래그 시작: 마우스 클릭
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)
        
        if mode == "circle":
            # 원 그리기
            cv2.circle(temp_image, (x, y), 70, (0, 255, 0), 2)
        elif mode == "line":
            # 선 그리기
            start_point = (x, y)  # 선 그리기 시작점 설정

    # 마우스 이동 중: 선 그리기
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if mode == "line":
            cv2.line(temp_image, start_point, (x, y), (255, 0, 0), 2)
            start_point = (x, y)

    # 드래그 종료: 마우스 버튼 뗄 때
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# 창 만들기 및 마우스 콜백 설정
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw)

# 이미지의 복사본을 생성해 수정된 내용만 반영
temp_image = image.copy()

while True:
    # 결과 이미지 보여주기
    cv2.imshow("Image", temp_image)

    # 'c'를 누르면 원 모드로 변경
    if cv2.waitKey(1) & 0xFF == ord('c'):
        mode = "circle"

    # 'l'을 누르면 선 모드로 변경
    elif cv2.waitKey(1) & 0xFF == ord('l'):
        mode = "line"

    # 'q'를 누르면 종료
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
