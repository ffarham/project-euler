import math

def f(n, power):
    sum = 0
    num = n
    length = int(math.log(n, 10)) + 1
    for i in range(length):
        x = num % 10
        sum += x ** power
        num = int(num//10)

    return sum == n

if __name__ == "__main__":

    power = input("power: ")
    total = 0
    for i in range(2, 1000000):
        if f(i, power) == True:
            print("i: ", i)
            total += i
    print("total: ", total)
