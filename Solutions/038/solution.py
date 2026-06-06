from tqdm import tqdm
from enum import Enum

class Result(Enum):
    YES = 'Y'
    NO = 'N'
    MAYBE = '?'
    

def is_pandigital(num: str) -> Result:
    num_set = set(num)
    if '0' in num_set: return Result.NO
    
    if len(num) < 9:
        return Result.MAYBE if len(num) == len(num_set) else Result.NO
    elif len(num) == 9:
        return Result.YES if len(num) == len(num_set) else Result.NO
    else:
        return Result.NO

ans = float('-inf')
for num in tqdm(range(1, 1_000_000)):
    concatenated_product = str(num)
    for n in range(2, 10):
        concatenated_product += str(num * n)
        result = is_pandigital(concatenated_product)
        if result == Result.NO: break
        elif result == Result.YES:
            ans = max(ans, int(concatenated_product))

print(f'Ans: {ans}')
