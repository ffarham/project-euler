if __name__ == "__main__":
    x = 200000000
    while True:
        check = 0
        for i in range(2,21):
            if x % i != 0: check += 1
        if check == 19:
            break
        x += 20
    print("Ans: " + str(x))