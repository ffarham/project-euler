

if __name__ == '__main__':
    n = 1
    for i in range(100):
        n *= 2 ** 10
    x = [i for i in str(n)]
    y = 0
    for j in range(len(x)):
        y += int(x[j])
    print(y)



