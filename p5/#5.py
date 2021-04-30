x = 200000000
while True:
    check = 0
    for k in range(2,21):
        if x % k == 0:
            check += 1
    if check == 19:
        print(x)
        break
    x += 20



