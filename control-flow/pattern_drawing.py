size = int(input("Enter the size of the pattern: "))
check = 0

while check != size:
    for j in range(size):
        print("*", end="")
    print("\n")
    check = check + 1