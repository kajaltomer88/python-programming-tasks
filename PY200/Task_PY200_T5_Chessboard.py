n = int(input("Enter value of N: "))

for row in range(n):
    for col in range(n):
        
        if row == col:
            print("X", end=" ")
        
        elif (row + col) % 2 == 0:
            print("1", end=" ")
        
        else:
            print("0", end=" ")
    
    print()   # new line after each row