# ','로 구분되어 있는 데이터를 Comma Separated Values라고 부른다
# -> csv
# 인공지능 처리, 데이터 처리가 활용 예

# BMI 데이터 만들기
# header: names, heights, weights
# "윤인성", 176, 65
# 램덤하게 1명의 키와 몸무게
# import random  # number = random.randrange(start, end): 랜덤값 = random.랜덤의범위(시작값, 끝값)
# hangul = list("가나다라마바사아자차카타파하")

# with open("file/human.csv", "w") as temp:
#     temp.write("이름, 몸무게, 키\n")
#     for _ in range(1000):
#         name = random.choice(hangul) + random.choice(hangul)
#         weight = random.randrange(40, 120)
#         heigh = random.randrange(140, 200)
#         temp.write(f"{name},{weight},{heigh}\n")

# BMI 분석하기
FILE = open("file/human.csv", "r")
print(FILE)
for bmi in FILE:
    name, weight, height = bmi.strip().split(',')
    if not weight.isdigit():  # if weight == "몸무게" and height == "키":
        continue
    weight, height = int(weight), int(height)
    bmi = weight / (height / 100) ** 2
    result = ""
    if bmi >= 25:
        result = "과체중"
    elif bmi >= 18.5:
        result = "정상체중"
    else:
        result = "저체중"
    print(f"이름: {name}\n몸무게: {weight}\n키: {height}\nBMI: {bmi:.2f}\n결과: {result}")
    print()
FILE.close()