x = int(input("give me a number? "))

for i in range(1,x + 1):
    for j in range(1, x + 1):
        print(i * j, end=' ')
    print("\n")