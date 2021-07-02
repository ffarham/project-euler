

def calc(n):
    x = 1
    for i in range(n, 0, -1):
        x *= i
    return x

if __name__ == '__main__':
    number = 100
    f = calc(number)
    a = [j for j in str(f)]
    ans = 0
    for k in range(len(a)):
        ans += int(a[k])
    print(ans)

