#checks if the given number is a palindrime
def isPalindrome(num): 
    #splits the num into an array of its digits
    numArr = []        
    while num != 0:
        digit = num % 10
        numArr.append(digit)
        num = int(num / 10)
    digitsArr = numArr[::-1]      #reverses the Arr
    for k in range(0,len(numArr)):      
        if numArr[k] != digitsArr[k]:
            return False
    return True

if __name__ == "__main__":     
    num = 0
    for i in range(100,1000):
        for j in range(100, 1000):
            product = i * j
            if isPalindrome(product):
                num = product if product > num else num            
    print("Ans: " + str(num))