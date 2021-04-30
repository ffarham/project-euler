def D(n):
    T = 0
    a = int(n/10)
    b = n % 10
    if a >= 2:
        T += double[a] + single[b]
    elif a >= 1:
        T += tens[b]
    else:
        T += single[b]
    return T



if __name__ == '__main__':
    single = [0,3,3,5,4,4,3,5,5,4]
    tens = [3,6,6,8,8,7,7,9,8,8]
    double = [0,0,6,6,5,5,5,7,6,6] #starting from 0
    hundred = 7
    thousand = 8
    And = 3

    total = 0

    #total += sum(single) + sum(tens)
    for i in range(1,1001):
        x = i % 100
        if i >= 100:
            if i == 1000:
                total += thousand + single[1]
            else:
                total += hundred
                h = int(i/100)
                total += single[h]

            if x != 0:
                total += And + D(x)
        else:
            total += D(x)
    print(total)


