def div(n):
    d = []
    m = int(n/2)
    for p in range(1,m+1):
        if n % p == 0:
            d.append(p)
    D = sum(d)
    if D > n:
        return True
    else:
        return False

if __name__ == '__main__':
    z = 28123
    Anumbers = []
    for k in range(1,z+1):
        if div(k) == True:
            Anumbers.append(True)
        else:
            Anumbers.append(False)
    AnumSum = 0
    total = 0
    for i in range(z):
        if Anumbers[i] == True:
            for j in range(z):
                if Anumbers[j] == True:
                    Asum = Anumbers[i] + Anumbers[j]
                    #if Asum not in AnumSum:
                    AnumSum += Asum

        for j in range(z):
            total += Anumbers[i] + Anumbers[j]


    print(total - Asum)


