# YOLOv8을 활용한 객체 탐지 모델 학습
from ultralytics.utils.downloads import download
from pathlib import Path
from ultralytics import YOLO

# 샘플 데이터셋 (COCO8) 다운로드
def down_image():
	url = "https://github.com/ultralytics/hub/raw/main/example_datasets/coco8.zip"
	download(url, dir=Path('../'))

	print("--- 다운로드 완료! 이제 폴더를 확인해 보세요 ---")

def yolo():
	model = YOLO("yolov8n.pt")  #YOLOv8 모델 로드
	model.train(data="data.yaml", epochs=5, imgsz=640)  # 사용자 데이터셋으로 학습

def main():
	down_image()
	yolo()

if __name__ == "__main__":
	main()