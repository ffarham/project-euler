# returns the greatest integer in the given array
def greatest(arr):
    greatest = 0
    for i in range(len(arr)):
        if arr[i] > greatest:
            greatest = arr[i]
    return greatest

if __name__ == "__main__":
    number = 600851475143  

    primeFactors = []       # stores all prime factors 
    while True:
        x = 1
        while x < 10000:
            x += 1
            if number % x == 0:
                factor = number / x
                primeFactors.append(x)
                number = factor
                x = 2000
        if number == 1:
            break
        
    print(greatest(primeFactors))
