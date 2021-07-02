if __name__ == "__main__":
    greatestPF, num = 0, 600851475143  

    while True:
        x = 1
        while True:
            x += 1
            if num % x == 0:
                factor = num / x
                greatestPF = x if x > greatestPF else greatestPF
                num = factor
                break
        if num == 1:
            break
        
    print("Ans: " + str(greatestPF))