import os
import cv2
import pytest  # 테스트 자동화
import numpy as np
from depth_map import generate_depth_map  # 소스 파일에서 함수 빌려옴

# 테스트 코드
def test_generate_depth_map():
	# 1. 검사 준비
	image = np.zeros((100, 100, 3), dtype=np.uint8)  # 검정색 빈 이미지 (100x100)

	# 2. 실행 : 가짜 이미지를 넣어 가짜 깊이 맵 생성
	depth_map = generate_depth_map(image)

	# 3. 검증 (깊이 맵 생성 함수 작동 검증)
	assert depth_map.shape == image.shape, "출력 크기가 입력 크기와 다릅니다."  # 픽셀 위치 어긋나면 안 되기 때문
	assert isinstance(depth_map, np.ndarray), "출력 데이터 타입이 ndarray가 아닙니다."  # 넘파이 배열 형식인지

# pytest 실행
if __name__ == "__main__":  # 이 파일이 직접 실행될 때만 작동
	# 1. 자동으로 테스트 (채점)
	print("--- 테스트를 시작합니다 ---")
	pytest.main([__file__])  # 현재 파일 (__file__)의 테스트 실행 (test_로 시작하는 함수들)

	# 2. 이미지 출력
	print("\n--- 실제 이미지를 화면에 출력합니다 ---")
	image = cv2.imread('../data/sample.jpg')  # 이미지 로드
	if image is not None:
		depth_result = generate_depth_map(image)

		# 폴더 생성
		if not os.path.exists('../output'):
			os.makedirs('../output')

		# 이미지 저장
		cv2.imwrite('../output/result_depth.jpg', depth_result)
		print("결과 이미지가 'result_depth.jpg'로 저장되었습니다.")

		cv2.imshow('Original Image', image)
		cv2.imshow('Depth Map', depth_result)
		cv2.waitKey(0)  # 키보드 입력이 있을 때까지 무한 대기
		cv2.destroyAllWindows()  # 현재 열려 있는 모든 OpenCV 창 닫기