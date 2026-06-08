from sympy import isprime
from typing import Iterator

def get_next_prime(num: int) -> Iterator[int]:
    while True:
        if isprime(num): yield num
        num += 1

def is_pandigital(num: int) -> bool:
    num_str = str(num)
    digit_set = set(num_str)
    for i in range(1, len(num_str)+1):
        if str(i) not in digit_set: return False
    return True

ans = float('-inf')
for p in get_next_prime(2):
    if len(str(p)) > 9: break
    if is_pandigital(p):
        if p > ans:
            print(f'New ans: {p}')
        ans = max(ans, p)
    