#Sieve Of Eratosthenes algorithm
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):     
        if (prime[p] == True):
            for i in range(p * p, n+1, p):  #marks all indexes that are multiple of prime numbers as false
                prime[i] = False
        p += 1

    #finds the 10001 prime number
    check = 0
    for p in range(2, n+1):
        if prime[p]:
            check += 1
            if check == 10001:
                return p

if __name__=='__main__':
    n = 1000000
    print("Ans: " + str(SieveOfEratosthenes(n)))