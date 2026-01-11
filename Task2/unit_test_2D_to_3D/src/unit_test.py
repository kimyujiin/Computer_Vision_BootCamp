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
	pytest.main()  # 이 파일 안에 있는 test_로 시작하는 함수들을 다 찾아서 테스트 시작