# 학습된 YOLOv8 모델을 사용한 객체 탐지
import cv2
from ultralytics import YOLO

# 1. 학습 완료된 모델 불러오기
model = YOLO("runs/detect/train/weights/best.pt") 

# 2. 테스트할 이미지 불러오기
image_path = "../data/test_image.jpg"
image = cv2.imread(image_path)

# 3. 객체 탐지 실행 (예측)
results = model(image)
for result in results:
	for box in result.boxes:
		x1, y1, x2, y2 = map(int, box.xyxy[0])  # 좌표값 변환
		label = result.names[int(box.cls[0])]  # 클래스 라벨
		confidence = box.conf[0]  # 신뢰도

		# 객체 경계 상자 그리기
		cv2.rectangle(image, (x1, y1), (x2, y2), (0,255, 0), 2)
		cv2.putText(image, f"{label}({confidence:.2f})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
	
	# 결과 출력
	cv2.imshow("YOLO ObjectDetection", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()