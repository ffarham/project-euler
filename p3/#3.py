primeFactors = [] 
number = 13195 

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
    
        

print(primeFactors)
