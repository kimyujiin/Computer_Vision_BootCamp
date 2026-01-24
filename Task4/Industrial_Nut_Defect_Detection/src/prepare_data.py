import os
import shutil

raw_data_path = '../data/raw/metal_nut' 
target_path = '../data/dataset'

def make_yolo_dataset(sub_folder, is_train=True):
	mode = 'train' if is_train else 'val'
	dest_img_dir = os.path.join(target_path, 'images', mode)
	dest_lbl_dir = os.path.join(target_path, 'labels', mode)
	os.makedirs(dest_img_dir, exist_ok=True)
	os.makedirs(dest_lbl_dir, exist_ok=True)

	src_dir = os.path.join(raw_data_path, sub_folder)
	folder_name = sub_folder.split('/')[-1] # bent, scratch 등

	for file_name in os.listdir(src_dir):
		if file_name.endswith('.png'):
			# 중복 방지를 위한 새 이름 생성
			new_file_name = f"{folder_name}_{file_name}"

			# 1. 이미지 복사
			shutil.copy(os.path.join(src_dir, file_name), 
				os.path.join(dest_img_dir, new_file_name))

			# 2. 라벨 파일 생성 (정상이면 0, 불량이면 1)
			label_name = new_file_name.replace('.png', '.txt')
			class_id = 0 if folder_name == 'good' else 1

			with open(os.path.join(dest_lbl_dir, label_name), 'w') as f:
				f.write(f"{class_id} 0.5 0.5 1.0 1.0")

# 실행부
make_yolo_dataset('train/good', is_train=True) # 학습용 정상
make_yolo_dataset('test/good', is_train=False)  # 검증용 정상

# 불량 폴더들 추가
for defect in ['bent', 'color', 'flip', 'scratch']:
	make_yolo_dataset(f'test/{defect}', is_train=False)