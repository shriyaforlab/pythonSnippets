prices = [107, 34, 67, 120]

discounts = list(map(lambda price: price * 0.90, prices))

upper_end = list(filter(lambda price: price > 50, prices))

print(discounts)
print(upper_end)