def prime(n):
    x = 2
    while x < len(n):
        if n[x] == True:
            for i in range(x+x,len(n), x):
                n[i] = False
        x += 1
    return(n)


if __name__ == '__main__':
    total = -1
    number = 2000000
    numbers = [True for i in range(number + 1)]
    PN = prime(numbers)
    for i in range(len(PN)):
        if PN[i] == True:
            total += i
    print(total)

