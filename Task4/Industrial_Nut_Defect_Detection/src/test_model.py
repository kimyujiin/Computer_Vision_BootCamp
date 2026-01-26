from ultralytics import YOLO
import cv2

# 1. 학습된 모델 불러오기
model = YOLO('../models/best.pt') 

# 2. 테스트할 이미지 경로
img_list = [
	'../data/dataset/images/val/test_good_rep0_014.png',
	'../data/dataset/images/val/test_color_rep0_020.png',
	'../data/dataset/images/val/test_flip_rep0_018.png'
]

# 3. 모델로 예측하기
results = model.predict(source=img_list, save=True, conf=0.25)

# 4. 결과 확인
for i, result in enumerate(results):
	print(f"--- Image {i+1} ---")
	print(f"Detected: {len(result.boxes)} objects")
	result.show()