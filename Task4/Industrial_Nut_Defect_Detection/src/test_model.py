from ultralytics import YOLO
import cv2

# 1. 학습된 모델 불러오기
model = YOLO('../models/best.pt') 

# 2. 테스트할 이미지 경로
img_path = '../data/dataset/images/val/scratch_002.png' 

# 3. 모델로 예측하기
results = model.predict(source=img_path, save=True, conf=0.25)

# 4. 결과 확인
for result in results:
	print(f"Detected: {len(result.boxes)} objects")
	result.show()