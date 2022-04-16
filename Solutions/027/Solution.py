def isPrime(x):
    for i in range(2, int(abs(x)**0.5)+1):
        if x % i == 0:
            return False
    return True

def f(a, b, n):
    return (n*n) + (a*n) + b

if __name__ == "__main__":
    coefficients = (0,0)
    product = 0
    max_n = 0
    for a in range(-999, 1000):
        if a % 100 == 0:  print(a)
        for b in range(-1000, 1001):
            n = 0
            while True:
                if not isPrime( f(a,b,n) ):
                    if n > max_n:
                        max_n = n
                        product = a * b
                        coefficients = (a,b)
                    break
                n += 1
  

    print("The coefficients " + str(coefficients) + " produce " + str(max_n) + " primes with product " + str(product))