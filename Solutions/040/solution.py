irrational_fraction = [ int(digit) for num in range(0, 200_000) for digit in str(num) ]

ans = irrational_fraction[1] \
    * irrational_fraction[10] \
    * irrational_fraction[100] \
    * irrational_fraction[1_000] \
    * irrational_fraction[10_000] \
    * irrational_fraction[100_000] \
    * irrational_fraction[1_000_000]

print(f'Ans: {ans}')