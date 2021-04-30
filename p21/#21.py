

def d(n):
    m = int(n/2)
    factors = []
    for k in range(1, m+1):
        if n % k  == 0:
            factors.append(k)
    ans = sum(factors)
    return ans



if __name__ == '__main__':
    total = 0
    num = 10000
    numbers = [False for i in range(num)]
    for j in range(num):
        if numbers[j] == False:
            a = j+1
            x = d(a)
            if x != a: #ensures number going in does not equal number going out
                b = d(x)
                if a == b:
                    numbers[j] = True
                    if b <= num:
                        numbers[b-1] = True
    for l in range(num):
        if numbers[l] == True:
            total += l+1
    print(total)

