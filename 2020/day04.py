def day04a():
    with open("2020/day04_input.txt", 'r') as f:
        passports = [
            [l.split(':')[0] for l in p.strip().replace('\n', ' ').split(' ')]
            for p in f.read().strip().split('\n\n')
        ]

    counter = 0
    for p in passports:
        counter += 1
        for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if k not in p:
                counter -= 1
                break
    
    return counter

def day04b():
    with open("2020/day04_input.txt", 'r') as f:
        passports = [
            {
                l.split(':')[0]:l.split(':')[1] 
                for l in p.strip().replace('\n', ' ').split(' ')
            }
            for p in f.read().strip().split('\n\n')
        ]

    def between(value, lbound, rbound):
        return value >= lbound and value <= rbound

    counter = 0
    for p in passports:
        if not all([k in p for k in 
                ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']]):
            continue
        if all([
            between(int(p['byr']), 1920, 2002),
            between(int(p['iyr']), 2010, 2020),
            between(int(p['eyr']), 2020, 2030),
            any([
                p['hgt'][-2:] == 'in' and between(int(p['hgt'][:-2]), 59, 76),
                p['hgt'][-2:] == 'cm' and between(int(p['hgt'][:-2]), 150, 193)
            ]),
            p['hcl'][0] == '#',
            len(p['hcl'][1:]) == 6,
            all([c in "0123456789abcdef" for c in p['hcl'][1:]]),
            p['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            len(p['pid']) == 9,
            all([d in "0123456789" for d in p['pid']])
        ]):
            counter += 1
    return counter

print(day04b())
