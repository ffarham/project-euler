def is_palindrome(string: str) -> bool:
    left_ptr, right_ptr = 0, len(string)-1
    while left_ptr <= right_ptr:
        if string[left_ptr] != string[right_ptr]: return False
        left_ptr += 1
        right_ptr -= 1
    return True

ans = 0
for num in range(1, 1_000_000):
    binary_representation = "{0:b}".format(num)
    if is_palindrome(str(num)) and is_palindrome(binary_representation):
        ans += num

print(f'Ans: {ans}')
