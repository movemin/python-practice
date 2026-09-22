A = [{
	"제목": "혼자 공부하는 파이썬",
	"가격": 18000
}, {
	"제목": "혼자 공부하는 머신러닝 + 딥러닝",
	"가격": 26000
}, {
	"제목": "혼자 공부하는 자바스크립트",
	"가격": 24000
}]

def price(item):
    return item["가격"]

print(min(A, key=price))
print(max(A, key=price))

# lambda
print(min(A, key = lambda item: item["가격"]))
print(max(A, key = lambda item: item["가격"]))

# sort
A.sort(key=lambda book: book["가격"])
print(A)