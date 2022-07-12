def square(amount):
    for num in range(1, amount + 1):
        yield num ** 2


squared = square(11)
print(next(squared))
print(next(squared))
for nums in squared:
    print(nums)


even = (n for n in range(10) if n % 2 == 0)
print(next(even))
print(next(even))
