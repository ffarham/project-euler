if __name__ == "__main__":
    for i in range(300):
        for k in range(500):
            for j in range(500):
                if i*i + k*k == j*j:
                    if i+j+k == 1000:
                        P = i*j*k
                        print("Ans: " + str(P))
                        exit()
