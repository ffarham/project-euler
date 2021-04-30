def sunday(x, n):
    a = x
    b = 0

    for i in range(len(n)):
        q = n[i] % 7
        a += q
        if a%7 == 0:
            b += 1
        if a>7:
            a -= 7

    z = [a, b]
    return z

if __name__ == '__main__':
    ans = 0
    day = 2
    for i in range(1901,2001):
        print(day)
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        if (i%4 == 0 and i%100 != 0) or (i%100 == 0 and i%400 == 0):
            months[1] = 29
            result = sunday(day, months)
            day = result[0]
            ans += result[1]

        else:
            result = sunday(day, months)
            day = result[0]
            ans += result[1]
    print(ans)


