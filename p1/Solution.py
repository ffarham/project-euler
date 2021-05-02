# returns true if the given int is a multiple of either 3 or 5 and false otherwise
def isMultiple(n):
    return n % 3 == 0 or n % 5 == 0

if __name__ == "__main__":
    sum = 0                             
    for i in range(1000):               
        if isMultiple(i) : sum += i     # updates the sum if i is a multiple
    print("Ans: " + str(sum))           