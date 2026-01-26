import os
import shutil
import random

raw_data_path = '../data/raw/metal_nut' 
target_path = '../data/dataset'

def prepare_balanced_dataset(folder_list):
	# 폴더 구조 초기화
	for mode in ['train', 'val']:
		os.makedirs(os.path.join(target_path, 'images', mode), exist_ok=True)
		os.makedirs(os.path.join(target_path, 'labels', mode), exist_ok=True)

	for sub_folder in folder_list:
		src_dir = os.path.join(raw_data_path, sub_folder)
		# 클래스 구분 (good : 0, defect : 1)
		folder_name = sub_folder.split('/')[-1]
		class_id = 0 if folder_name == 'good' else 1

		# 이미지 파일 목록 가져오기
		images = [f for f in os.listdir(src_dir) if f.endswith('.png')]
		random.shuffle(images)

		# 8:2 분할 계산 (train / val)
		split_idx = int(len(images) * 0.8)
		train_files = images[:split_idx]
		val_files = images[split_idx:]

		# 파일 복사
		for files, mode in [(train_files, 'train'), (val_files, 'val')]:
			# 오버샘플링
			repeat_count = 5 if (mode == 'train' and class_id == 1) else 1

			for i in range(repeat_count):
				for file_name in files:
					parent_name = sub_folder.split('/')[0]
					new_name = f"{parent_name}_{folder_name}_rep{i}_{file_name}"

					# 이미지 복사
					shutil.copy(os.path.join(src_dir, file_name),
							os. path.join(target_path, 'images', mode, new_name))

					# 라벨 생성
					label_name = new_name.replace('.png', '.txt')
					with open(os.path.join(target_path, 'labels', mode, label_name), 'w') as f:
						f.write(f"{class_id} 0.5 0.5 1.0 1.0")

	print(f"오버샘플링 포함 데이터 구축 완료")

my_folders = ['train/good', 'test/good', 'test/bent', 'test/color', 'test/flip', 'test/scratch']
prepare_balanced_dataset(my_folders)