import cv2
import pytesseract

# Tesseract 경로 (백슬래시를 raw string 형식으로 처리)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 흑백 변환
gray_image = cv2.imread("receipt.png", cv2.IMREAD_GRAYSCALE)

# Tesseract를 이용해서 이미지에서 텍스트를 추출
text = pytesseract.image_to_string(gray_image, lang="kor")

print("추출된 텍스트: ", text)

# 자동차 번호 인식
gray_car = cv2.imread("car.png", cv2.IMREAD_GRAYSCALE)

# 블러
blur = cv2.GaussianBlur(gray_car, (5,5), 0)

# 이진화 처리
thresh =  cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)

# AdaptiveThreshold: 적응형 메서드(Threshold: 고정형 메서드)
# blockSize: 각 픽셀의 임계값을 계산할 때 참조할 이웃 영역의 크기. 무조건 홀수
# C: 계산된 임계값에서 차감할 상수

text = pytesseract.image_to_string(thresh, lang = "kor", config = "--psm 6")
# config: page 분할 모드

print(text)