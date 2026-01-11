import cv2
import numpy as np

# 샘플 함수 : 가짜 깊이 맵 생성
def generate_depth_map(image):
	if image is None:
		raise ValueError("입력된 이미지가 없습니다.")

	# 컬러 → 흑백 (이미지 행렬)
	grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	# 가짜 깊이 맵 적용
	depth_map = cv2.applyColorMap(grayscale, cv2.COLORMAP_JET)  # 무지개색 시각화

	return depth_map