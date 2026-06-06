from tqdm import tqdm
from sympy import isprime

def is_truncatable_prime(num: int) -> bool:    
    num_str = str(num)
    for i in range(len(num_str)):
        if not isprime(int(num_str[i:])): return False
        if not isprime(int(num_str[:len(num_str)-i])): return False
    return True

count, ans = 0, 0
for num in tqdm(range(11, 1_000_000)):
    if is_truncatable_prime(num):
        ans += num
        count += 1
    num += 1

print(f'Found {count} truncatable primes.\nAns: {ans}')
