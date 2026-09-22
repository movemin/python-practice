products = [("노트북", 1200000), ("키보드", 85000), ("마우스", 35000), ("모니터", 300000)]
print(list(filter(lambda price: price[1] >= 100_000, products)))