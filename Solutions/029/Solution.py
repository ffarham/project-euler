def f(a, b):
    numbers = set()
    for i in range(a, b+1):
        for j in range(a, b+1):
            x = len(numbers)
            numbers.add(i**j)
            if x == len(numbers):
                print(i**j)
            ##print(i, j)
    print(len(numbers))

if __name__ == "__main__":
    n = input("n: ")
    f(2, n);
