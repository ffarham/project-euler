

def dpAlgorithm(n, coins):
    ways = [1] + [0] * n
    for c in coins:
        for i in range(n+1-c):
            ways[i+c] += ways[i]
    return ways[-1]

if(__name__ == "__main__"):
    n = 200
    coins = [1,2,5,10,20,50,100,200]
    total = dpAlgorithm(n, coins)
    print total