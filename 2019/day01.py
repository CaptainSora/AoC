def day01a():
    with open("2019/day01_input.txt", 'r') as f:
        masses = f.read().strip().split('\n')
    
    total_fuel = 0
    for mass in masses:
        total_fuel += int(int(mass)/3)-2
    return total_fuel

def day01b():
    with open("2019/day01_input.txt", 'r') as f:
        masses = f.read().strip().split('\n')
    
    total_fuel = 0
    for mass in masses:
        fuel = int(int(mass)/3)-2
        while (fuel > 0):
            total_fuel += fuel
            fuel = int(fuel/3)-2
    return total_fuel

print(day01b())