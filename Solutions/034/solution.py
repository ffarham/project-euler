import math

FACTORIAL_MAP = {}
for i in range(10):
    FACTORIAL_MAP[i] = math.factorial(i)

MAX_NUM = 1_000_000

factorial_sum = lambda num: sum([FACTORIAL_MAP[int(digit_str)] for digit_str in str(num)])
ans = sum([ num for num in range(3, MAX_NUM) if factorial_sum(num) == num])
print(f'Ans: {ans}')
