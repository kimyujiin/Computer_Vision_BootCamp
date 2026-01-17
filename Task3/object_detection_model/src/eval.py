# 모델 평가 방법
from ultralytics import YOLO
import matplotlib.pyplot as plt

# 1. 만든 모델 불러오기
model = YOLO("runs/detect/train/weights/best.pt")

# 2. 검증 데이터로 성능 평가
metrics = model.val()
# print(metrics)

# 3. 주요 수치 출력
print(f"정확도(mAP50): {metrics.box.map50:.3f}")  # 0.5 이상의 정확도로 맞힌 비율
print(f"정밀도(Precision): {metrics.box.mp:.3f}")  # 찾은 것 중 진짜 정답인 비율
print(f"재현율(Recall): {metrics.box.mr:.3f}")  # 실제 정답 중 찾아낸 비율

# 4. Matplotlib을 활용한 성능 평가 시각화
# 4-1. Precision, Recall 그래프 출력
p = metrics.box.mp   # Mean Precision
r = metrics.box.mr   # Mean Recall
map50 = metrics.box.map50 # mAP50

# 4-2. 막대 그래프 등으로 시각화하기
labels = ['Precision', 'Recall', 'mAP50']
values = [p, r, map50]

plt.bar(labels, values, color=['blue', 'green', 'red'])
plt.ylim(0, 1.1)
plt.title("Model Evaluation Metrics")
for i, v in enumerate(values):
    plt.text(i, v + 0.02, f"{v:.3f}", ha='center')
plt.show()