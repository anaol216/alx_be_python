size = int(input("Enter the size of the pattern: "))
initial = 1
while initial <= size:
    for space in range(1,size):
        print("* ", end="")
    print()
    initial += 1
    