def even(n):
    return n/2

def odd(n):
    return (3*n)+1

if __name__ == '__main__':
    appeared = []
    z = 0
    x = 0
    for i in range(1,1000000):
        y = 0
        a = i
        while a != 1:

            if i not in appeared:
                if a % 2 == 0:
                    a = even(a)
                    y += 1
                else:
                    a = odd(a)
                    y += 1
                #appeared.append(i)
        if y > x:
            x = y
            z = i
    print(z)