def day01a():
    with open("2017/day01_input.txt", 'r') as f:
        digits = f.read().strip()
    
    total = 0
    for i in range(len(digits)):
        if digits[i] == digits[i-1]:
            total += int(digits[i])
    
    return total

def day01b():
    with open("2017/day01_input.txt", 'r') as f:
        digits = f.read().strip()
    
    half = int(len(digits)/2)
    total = 0
    for i in range(len(digits)):
        if digits[i] == digits[i-half]:
            total += int(digits[i])
    
    return total


print(day01a())
print(day01b())
