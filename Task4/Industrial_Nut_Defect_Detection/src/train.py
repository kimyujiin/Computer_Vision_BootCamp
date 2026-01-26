from ultralytics import YOLO

# 1. 모델 불러오기
model = YOLO('yolov8n.pt') 

# 2. 학습 시작
results = model.train(
	data='../data/data.yaml',  # 설정 파일 경로
	epochs=100,  # 전체 데이터를 반복 학습 횟수
	imgsz=640,  # 이미지 크기
	batch=-1,  # 한 번에 학습할 이미지 개수 (최적 배치 사이즈)
	name='nut_defect_model',  # 결과가 저장될 폴더 이름
	device=0,  # T4 GPU
	patience = 20,  # 성능 향상이 없으면 20회 후에 조기 종료
	augment = True  # 학습 중 무작위 변환을 추가해 일반화 성능 강화
)