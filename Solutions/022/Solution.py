


if __name__ == '__main__':
    file = open("#22_.txt", "r")
    f = file.read()
    f = f.replace('"', '')
    names = f.split(",")

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sortedNames = sorted(names, key = str.lower)

    ans = 0
    for i in range(len(sortedNames)):
        name = sortedNames[i]
        position = int(i+1)
        value = 0
        for j in range(len(name)):
            alpha = name[j].lower()
            for k in range(len(alphabet)):
                if alphabet[k] == alpha:
                    value += k+1
        ans += (position*value)
    print(ans)



