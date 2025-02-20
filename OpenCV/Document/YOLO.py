from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt") # YOLO모델 v8, n: nano버전

image = cv2.imread("YOLO_test.webp")

# 객체 탐지 
model.predict(source = image,
              save=False,
              save_txt = False, 
              conf=0.5 # conf: 신뢰도 임계값(Threshold)
              )