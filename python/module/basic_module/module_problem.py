# 모듈을 읽어 들입니다.
import os

# 현재 폴더의 파일/폴더를 출력합니다.
# 현재 실행되고 있는 경로에 들어 있는 폴더나 파일을 리스트 형식으로 출력
output = os.listdir(".")
print("os.listdir():", output)
print()

# 현재 폴더의 파일/폴더를 구분합니다.
print("# 폴더와 파일 구분하기")
for path in output:
    if os.path.isdir(path):
        print("폴더:", path)
    else:
        print("파일:", path)

# 문제: 폴더라면 또 탐색하기 라는 재귀 구성으로
# 현재 폴더 내부에 있는 모든 파일을 탐색해보자.
def read_folder(path):
    output = os.listdir(path)
    for item in output:
        if os.path.isdir(item):
            read_folder(item)
        else:
            print(f"{item}")

read_folder(".")