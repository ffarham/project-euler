number = 0

def check(num): 
    numList = []        
    while num >= 10:
        digit = num % 10
        numList.append(digit)
        num = int(num / 10)
    numList.append(num)
    digitsList = numList[::-1]
    test = 0
    for k in range(0,len(numList)):
        if numList[k] == digitsList[k]:
            test += 1
    if test == len(numList):
        return True
        
    
for i in range(1,1000):
    for n in range(1, 1000):
        product = i * n
        length = len(str(product))
        if product >= 10:
            if check(product) == True:
                if product > number:
                    number = product
        
print(number)
    
     



        
 
            
