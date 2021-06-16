sumofsquares = 0
squareofsum = 0

number = 100

for i in range(1, number+1):
    squareofsum += i
    sumofsquares += i*i
squareofsum *= squareofsum
print(squareofsum)
print(sumofsquares)

ans = squareofsum - sumofsquares
print(ans)
