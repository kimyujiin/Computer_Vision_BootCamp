import os
from datasets import load_dataset
from PIL import ImageFilter, ImageOps, ImageEnhance  # 이미지 필터, 작업, 보정
import numpy as np
import shutil  # 파일 복사

# 경로 설정
base_path = 'C:/Users/kyi13/Desktop/Computer_Vision_Task/Task1/image-preprocessing-outlier-filter'
raw_path = os.path.join(base_path, 'data')
prep_path = os.path.join(base_path, 'preprocessed-data')
sample_path = os.path.join(base_path, 'preprocessed_samples')

# 폴더가 없으면 생성
for path in [raw_path, prep_path, sample_path]:
	if not os.path.exists(path):
		os.makedirs(path)

# 데이터셋에서 이미지 로드
dataset = load_dataset("ethz/food101", split="train", streaming=True)

# 전처리 및 이상치 처리
for i, data in enumerate(dataset):  # enumerate => (번호, 내용)
	if i >= 200: break  # 200장

	# --- 원본 이미지 저장 ---
	raw_image = data['image'].convert("RGB")  # 이미지 객체 로드 및 RGB 포맷으로 변경 (투명도, 흑백 사진 에러 보호)
	raw_image.save(os.path.join(raw_path, f"raw_{i}.jpg"))  # 이미지 저장

	# --- 전처리 1단계 ---
	# 1. 크기 조정 (224x224)
	resized = raw_image.resize((224, 224))

	# 2-1. 색상 변환 (Grayscale)
	gray_img = resized.convert("L")
	# 2-2. Normalize
	img_array = np.array(gray_img)
	normalized_img = img_array / 255.0

	# --- 심화문제 1. 너무 어두운 이미지 제거 ---
	avg_brightness = np.mean(img_array)  # 평균 밝기 계산 (0~255)
	threshold = 80  # 기준값 설정
	if avg_brightness < threshold:
		print(f"Skipping image {i}: Too dark (Avg: {avg_brightness:.2f})")
		continue  # 다음 이미지로 점프 (저장 x)

	# --- 심화문제 2. 객체 크기가 너무 작은 이미지 제거 ---
	object_pixel_count = np.sum(img_array > 110)  # 밝기가 110보다 큰 부분의 합 개수
	object_ratio = object_pixel_count / 50176  # 밝은 부분 (음식) / 전체 (224x224 = 50176)
	if object_ratio < 0.3:  # 30%보다 작으면
		print(f"Skipping image {i}: Object too small (Object Ratio: {object_ratio:.2f})")
		continue  # 다음 이미지로 점프

	# --- 전처리 2단계 ---
	# 3. 노이즈 제거 (가우시안 블러 필터)
	blurred_img = gray_img.filter(ImageFilter.GaussianBlur(radius=1))

	# --- 전처리 이미지 저장 ---
	blurred_img.save(os.path.join(prep_path, f"prep_{i}.jpg"))

	# 4-1. 데이터 증강 (좌우 반전)
	flipped_img = ImageOps.mirror(blurred_img)
	flipped_img.save(os.path.join(prep_path, f"prep_{i}_flipped.jpg"))
	# 4-2. 데이터 증강 (회전)
	rotated_img = blurred_img.rotate(30)  # 30도
	rotated_img.save(os.path.join(prep_path, f"prep_{i}_rotated.jpg"))
	# 4-3. 데이터 증강 (색상 변화)
	brightness_tool = ImageEnhance.Brightness(blurred_img)  # 밝기 조절기 준비
	bright_img = brightness_tool.enhance(1.5)  # 1.5배 밝게
	dim_img = brightness_tool.enhance(0.5)  # 0.5배 어둡게

	# --- 전처리 + 증강 이미지 저장 ---
	bright_img.save(os.path.join(prep_path, f"prep_{i}_bright.jpg"))  # 저장
	dim_img.save(os.path.join(prep_path, f"prep_{i}_dim.jpg"))
	print(f"Save prep_{i}.jpg, prep_{i}_flipped.jpg, prep_{i}_rotated.jpg, prep_{i}_bright.jpg, prep_{i}_dim.jpg")

# preprocessed_samples
all_files = sorted(os.listdir(prep_path), key=lambda x: int(x.split('_')[1].split('.')[0]))  # 전처리 폴더에 저장된 파일 정렬

sample_files = []
for idx in [0, 6, 12, 18, 24]:  # 5장 복사
	if idx < len(all_files):
		sample_files.append(all_files[idx])

for file_name in sample_files:  # 저장
	src = os.path.join(prep_path, file_name)
	dst = os.path.join(sample_path, file_name)
	shutil.copy(src, dst)
	print(f"Sample Selected: {file_name}")