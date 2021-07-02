if __name__ == "__main__":
    evenSum, newValue, x, y = 0, 0, 1, 1
    while newValue <= 4000000:
        newValue = x + y
        if newValue % 2 == 0:
            evenSum += newValue
        y = x
        x = newValue
    print("Ans: " + str(evenSum))