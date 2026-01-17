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

# 자동 테스트 실행
def run_unit_test():
	print("--- 테스트를 시작합니다 ---")
	pytest.main([__file__])


# 이미지와 깊이 맵을 3D 좌표와 색상 데이터로 변환
def convert_to_3d_points(image, depth_result):
	# 3D 포인트 클라우드 변환 (평면을 점 구름인 입체 형상으로)
	h, w = depth_result.shape[:2]  # 이미지의 높이, 너비 픽셀 수
	X, Y = np.meshgrid(np.arange(w), np.arange(h))  # X : 모든 점의 가로 위치, Y : 모든 점의 세로 위치 적힌 표
	grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	Z = grayscale.astype(np.float32)  # Depth 값을 Z 축으로 사용 (흑백 이미지의 밝기값)

	# 3D 좌표 생성
	points_3d = np.dstack((X, Y, Z))  # 같은 위치의 X, Y, Z 값을 3차원 배열로

	color_data = cv2. cvtColor(depth_result, cv2.COLOR_BGR2RGB) / 255.0  # 색상 데이터

	return points_3d, color_data

# 3D 좌표와 색상 데이터를 .obj 파일로 저장
def save_points_as_obj(points_3d, color_data, obj_path):
	h, w = points_3d.shape[:2]
	
	with open(obj_path, 'w') as f:  # 쓰기 모드
		# 1) 모든 점 (Vertex) + 색상 기록
		for i in range(h):  # 줄
			for j in range(w):  # 칸
				p = points_3d[i, j]  # (i, j) 점
				c = color_data[i, j]  # (i, j) 색깔
				f.write(f"v {p[0]} {p[1]} {p[2]} {c[0]} {c[1]} {c[2]}\n")

		# 2) 점들을 연결해서 면 (Face) 만들기
		for i in range(h - 1):  # 이미지 세로
			for j in range(w - 1):  # 이미지 가로
				v1 = i * w + j + 1  # 현재 점
				v2 = i * w + j + 2  # 오른쪽 점
				v3 = (i + 1) * w + j + 1  # 아래쪽 점
				v4 = (i + 1) * w + j + 2  # 오른쪽 아래 점
				f.write(f"f {v1} {v3} {v2}\n")  # 세 점을 연결해서 삼각형 면 만듦
				f.write(f"f {v2} {v3} {v4}\n")  # 삼각형 면 (3D 그래픽 면의 가장 기본 단위)
	print(f"\n--- {obj_path} 파일을 3D 뷰어로 열어보세요. ---")


def main():
	# 1. 테스트 실행
	run_unit_test()

	# 2. 이미지 로드 및 폴더 생성
	image = cv2.imread('../data/sample.jpg')  # 이미지 로드
	if image is None: return
	os.makedirs('../output', exist_ok=True)

	# 3-1. 데이터 변환
	depth_result = generate_depth_map(image)

	# 3-2. 깊이 맵 이미지 저장
	cv2.imwrite('../output/result_depth.jpg', depth_result)
	print("\n--- 결과 이미지가 'result_depth.jpg'로 저장되었습니다 ---")

	# 3-3. 3차원 좌표 생성 및 색상 생성
	points_3d, color_data = convert_to_3d_points(image, depth_result)

	# 4. 파일 저장
	obj_path = os.path.join('../output', 'result_3d.obj')
	save_points_as_obj(points_3d, color_data, obj_path)

	# 5. 이미지 출력
	cv2.imshow('Original Image', image)
	cv2.imshow('Depth Map', depth_result)
	cv2.waitKey(0)  # 키보드 입력이 있을 때까지 무한 대기
	cv2.destroyAllWindows()  # 현재 열려 있는 모든 OpenCV 창 닫기
	
# pytest 실행
if __name__ == "__main__":  # 이 파일이 직접 실행될 때만 작동
	main()