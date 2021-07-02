if __name__ == "__main__":
    sumofsquares, sum = 0, 0
    for i in range(1, 101):
        sum += i
        sumofsquares += i*i
    squareofsum = sum * sum

    print("Ans: " + str(squareofsum - sumofsquares))
