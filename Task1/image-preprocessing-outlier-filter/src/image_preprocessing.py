import os
from datasets import load_dataset
from PIL import ImageFilter, ImageOps, ImageEnhance  # 이미지 필터, 작업, 보정
import numpy as np

# 경로 설정
base_path = 'C:/Users/kyi13/Desktop/Computer_Vision_Task/Task1/image-preprocessing-outlier-filter'
raw_path = os.path.join(base_path, 'data')
prep_path = os.path.join(base_path, 'preprocessed-data')

# 폴더가 없으면 생성
for path in [raw_path, prep_path]:
        if not os.path.exists(path):
                os.makedirs(path)

# 데이터셋에서 이미지 로드
dataset = load_dataset("ethz/food101", split="train", streaming=True)

# 전처리 및 이상치 처리
for i, data in enumerate(dataset):  # enumerate => (번호, 내용)
        if i >= 20: break  # 20장

        # --- 원본 이미지 저장 ---
        raw_image = data['image'].convert("RGB")  # 이미지 객체 로드 및 RGB 포맷으로 변경 (투명도, 흑백 사진 에러 보호)
        raw_image.save(os.path.join(raw_path, f"raw_{i}.jpg"))  # 이미지 저장

        # --- 전처리 ---
        # 1. 크기 조정 (224x224)
        resized = raw_image.resize((224, 224))

        # 2-1. 색상 변환 (Grayscale)
        gray_img = resized.convert("L")
        # 2-2. Normalize
        img_array = np.array(gray_img)
        normalized_img = img_array / 255.0

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
