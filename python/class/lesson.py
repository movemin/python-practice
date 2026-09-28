# 학생들의 성적을 저장해두고
# 평균과 합계를 출력하는 프로그램
# students = [
#     {"이름": "인성", "국어": 87, "영어": 88, "수학": 98, "과학": 95},
#     {"이름": "구름", "국어": 92, "영어": 98, "수학": 97, "과학": 98},
#     {"이름": "별이", "국어": 76, "영어": 96, "수학": 95, "과학": 90}
# ]

# print("이름", "총점", "평균", sep="\t")
# for student in students:
#     score = student["국어"] + student["영어"] + student["수학"] + student["과학"]
#     average = score // (len(student) - 1)
#     print(student["이름"], score, average, sep="\t")

# 1번 해결
def create_student(name, korean, english, math, science):
    return {"이름": name, 
				    "국어": korean, 
				    "영어": english, 
				    "수학": math, 
				    "과학": science}

# 2번 해결
def sum_student(student):
	return student["국어"] + student["영어"] + student["수학"] + student["과학"]
	
def average_student(student):
	return sum_student(student) / 4


# main 코드
students = [
        create_student("인성", 87, 88, 98, 95),
        create_student("구름", 92, 98, 97, 98),
        create_student("별이", 76, 96, 95, 90)
]

# 만약 'students'라는 변수에 아예 접근하지 못하게 만들었다면 "총점과 평균을 구하는 코드를 작성하는 행위' 자체를 불가능하게 만들 수 있을 것입니다.
for student in students:
	total = sum_student(student)
	average = average_student(student)
	print(student["이름"], total, average, sep="\t")