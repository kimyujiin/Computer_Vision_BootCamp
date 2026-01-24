from ultralytics import YOLO

# 1. 모델 불러오기
model = YOLO('yolov8n.pt') 

# 2. 학습 시작
results = model.train(
	data='../data/data.yaml',  # 설정 파일 경로
	epochs=50,  # 전체 데이터를 반복 학습 횟수
	imgsz=640,  # 이미지 크기
	batch=4,  # 한 번에 학습할 이미지 개수
	workers = 0,  # 충돌 방지
	name='nut_defect_model',  # 결과가 저장될 폴더 이름
	device='cpu'  # GPU가 없다면 'cpu', 있다면 0
)