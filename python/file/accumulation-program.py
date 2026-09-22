# 입력 누적 프로그램
with open("file/accumulation-program.txt", "r") as my_file:
    output = my_file.read()
    if output:
        print(output.strip().split('\n'))

data = input("> 데이터를 입력해주세요: ")

with open("file/accumulation-program.txt", "a") as my_file:
    my_file.write(data + "\n")