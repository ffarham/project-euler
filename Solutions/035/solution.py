import sympy

MAX_NUM = 1_000_000

def get_rotations(num):
    rotations = []
    num_str = str(num)
    for _ in range(len(num_str)):
        num_str += num_str[0]
        num_str = num_str[1:]
        rotations.append(int(num_str))
    return rotations
        

ans = 0
for num in range(MAX_NUM):
    is_circular_prime = True
    for rotation in get_rotations(num):
        if not sympy.isprime(rotation):
            is_circular_prime = False
            break
    if is_circular_prime: ans += 1

print(f'Ans:{ans}')