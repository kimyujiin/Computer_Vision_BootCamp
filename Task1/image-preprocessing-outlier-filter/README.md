# Computer Vision Task 1 Extra : 이미지 전처리 및 이상치 탐지 필터링

이 프로젝트는 Hugging Face 데이터셋에서 이미지를 가져와 AI 학습 전 이미지 전처리를 수행합니다.

---

## 주요 기능

* **전처리 - 이미지 크기 조정** : 모든 이미지 해상도를 통일하여 연산 효율 높이기
* **전처리 - Grayscale 색상 변환** : 색상 정보보다 형태적 특징이 중요하므로 흑백 채널로 변환하고, 픽셀 값을 정규화
* **전처리 - 노이즈 제거 (가우시안 블러)** : 필터를 적용하여 고주파 노이즈를 억제하고 이미지의 핵심적인 윤곽 특징 강조
* **전처리 - 데이터 증강** : 모델 일반화 성능 향상을 위해 좌우 반전, 회전 (30도), 밝기 조절 (0.5배, 1.5배) 변형 추가
* **이상치 탐지 필터 - 어두운 이미지 제거** : 평균 밝기가 80 미만인 이미지를 데이터셋에서 제외
* **이상치 탐지 필터 - 객체 크기가 작은 이미지 제거** : 전체 픽셀 대비 밝은 영역 (음식 객체)의 비율이 30% 미만인 사진 필터링

## 파일 구조

* `image-processing-outlier-filter/src/image_preprocessing.py` : 이미지 전처리 및 이상치 탐지 필터링 소스 코드
* `image-processing-outlier-filter/data/raw_*` : 전처리 전 원본 이미지 데이터셋 (200장)
* `image-processing-outlier-filter/preprocessed-data/prep_*` : 전처리 및 필터링 된 이미지
* `image-processing-outlier-filter/preprocessed_samples/prep_*` : 전처리 및 필터링 된 이미지 중 대표 샘플 이미지 (5장)

---

## 실행 방법
1. 관련 라이브러리 설치 :
```bash
pip install datasets pillow numpy
```
2. 스크립트 실행 :
```bash
# src 폴더로 이동 후 실행
python image_preprocessing.py
```

---

## 결과 화면
- 원본
| :---: | :---: | :---: |
| ![원본 이미지 0](./data/raw_0.jpg) | ![원본 이미지 1](./data/raw_1.jpg) | ![원본 이미지 2](./data/raw_2.jpg) |

| :---: | :---: |
| ![원본 이미지 3](./data/raw_3.jpg) | ![원본 이미지 4](./data/raw_4.jpg) |

- 전처리
| 전처리 | 밝게 | 어둡게 |
| :---: | :---: | :---: |
| ![전처리 이미지 0](./preprocessed_samples/prep_0.jpg) | ![전처리 이미지 1](./preprocessed_samples/prep_1_bright.jpg) | ![전처리 이미지 2](./preprocessed_samples/prep_2_dim.jpg) |

| 좌우 반전 | 30도 회전 |
| :---: | :---: |
| ![전처리 이미지 3](./preprocessed_samples/prep_3_flipped.jpg) | ![전처리 이미지 4](./preprocessed_samples/prep_4_rotated.jpg) |