def grid(n):
    G = []
    for i in range(n+1):
        g = []
        for k in range(n+1):
            g.append(0)
        G.append(g)
    return G


if __name__ == '__main__':
    n = 20
    G = grid(n)

    for i in range(n+1):
        G[n][i] = 1
        G[i][n] = 1


    for j in range(n-1, -1, -1):
        for k in range(n-1, -1, -1):
            G[j][k] = G[j+1][k] + G[j][k+1]

    print(G[0][0])
