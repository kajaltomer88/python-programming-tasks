n = int(input("Enter value of N: "))

def is_valid(x):
    s = str(x)
    
    # Rule 1: No digit 0
    if '0' in s:
        return False
    
    # Rule 2: Exactly two 3s
    if s.count('3') != 2:
        return False
    
    # Rule 3: Sum of digits divisible by 7
    digit_sum = sum(int(d) for d in s)
    if digit_sum % 7 != 0:
        return False
    
    return True


found = False

for x in range(1, n + 1):
    if is_valid(x):
        print(x)
        found = True
        break

if not found:
    print(-1)