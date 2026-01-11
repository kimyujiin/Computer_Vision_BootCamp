# Computer Vision Task Repository

이 저장소는 컴퓨터 비전 부트캠프의 과제들을 정리하는 공간입니다.

---

## 과제 목록

### Task 1 : 픽셀 단위 이미지 처리 & 전처리 및 이상치 처리 필터링

* **설명** : 픽셀 단위 이미지로부터 빨간색 검출 필터, Food101 데이터셋을 활용한 이미지 전처리 및 밝기/객체 비율 기반 필터링 구현
* **Task 1** : [빨간색 검출 필터](./Task1/image-processing/README.md)
* **Task 1 Extra** : [이미지 전처리 및 이상치 탐지 필터링](./Task1/image-preprocessing-outlier-filter/README.md)

### Task 2 : Unit Test 구성 2D → 3D 변환 실습

* **설명** : 이미지 밝기 데이터를 깊이 정보 (Z)로 변환하여 컬러 3D 메쉬 (.obj)를 생성하고, pytest를 이용한 테스트 자동화 파이프라인 구축
* **Task 2** : [Unit Test 구성 2D → 3D 변환 실습](./Task2/unit_test_2D_to_3D/README.md)

---

## 기술 스택

* **Language** : Python
* **Library** : OpenCV, Pillow, Numpy, Hugging Face Datasets, Pytest (Unit Testing)
* **Tools** : [3DViewer.net](https://3dviewer.net/) (3D Model Visualization)