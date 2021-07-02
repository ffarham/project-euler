def SieveOfEratosthenes(n):

    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    check = 0
    for p in range(2, n+1):
        if prime[p]:
            check += 1
            if check == 10001:
                print (p),

# driver program
if __name__=='__main__':
    n = 1000000
    SieveOfEratosthenes(n)