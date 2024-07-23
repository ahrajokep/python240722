import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\student\Downloads'

# 이동할 폴더 경로
folders = {
    'images': ['*.jpg', '*.jpeg'],
    'data': ['*.csv', '*.xlsx'],
    'docs': ['*.txt', '*.doc', '*.pdf'],
    'archive': ['*.zip']
}

# 폴더 생성 함수
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 파일 이동 함수
def move_files(source_folder, destination_folder, patterns):
    for pattern in patterns:
        for file in glob.glob(os.path.join(source_folder, pattern)):
            shutil.move(file, destination_folder)

# 메인 실행 함수
def main():
    for folder, patterns in folders.items():
        destination_path = os.path.join(download_folder, folder)
        create_folder(destination_path)
        move_files(download_folder, destination_path, patterns)

if __name__ == '__main__':
    import glob
    main()
