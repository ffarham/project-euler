evenSum = 0
newValue = 0
x = 1
y = 1
while newValue <= 4000000:
    newValue = x + y
    if newValue%2 == 0:
        evenSum += newValue
    y = x
    x = newValue
print(evenSum)
    
    
    
