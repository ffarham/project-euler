import math
def factor(n):

    factors = 0
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            factors += 1
    factors *= 2
    return factors

if __name__ == '__main__':

    x = 1
    while True:
        T = 0
        for i in range(1,x+1):
            T += i
        factors = factor(T)
        if factors > 500:
            print("Final ans: ", T)
            break

        x += 1





