from tqdm import tqdm

ans = None
max_solution_count = float('-inf')
for p in tqdm(range(1, 1_000)):
    solution_count = 0
    for a in range(1, p-2):
        for b in range(a+1, p-a-1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solution_count += 1
    if solution_count > max_solution_count:
        max_solution_count = solution_count
        ans = p

print(f'Ans: {ans} with {max_solution_count} solutions.')