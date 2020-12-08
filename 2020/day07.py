def day07a():
    with open("2020/day07_input.txt", 'r') as f:
        bagreqs = [
            [word.strip() for word in
            rule.strip().replace(',', '').replace('.', '').replace('bags', '')\
                .replace('bag', '').replace('contain ', '').split(' ')
            if word != '' and not word.isnumeric()]
            for rule in f.read().strip().split('\n')]
    bagreqs = [
        [' '.join(rule[i:i+2]) for i in range(len(rule)) if i % 2 == 0]
        for rule in bagreqs]
    
    holders = ["shiny gold"]
    while True:
        change = False
        for rule in bagreqs:
            if rule[0] in holders:
                continue
            for b in holders:
                if b in rule[1:]:
                    holders.append(rule[0])
                    change = True
                    break
        if not change:
            break
    return len(holders) - 1

def day07b():
    with open("2020/day07_input.txt", 'r') as f:
        bagreqs = [
            [word.strip() for word in
            rule.strip().replace(',', '').replace('.', '').replace('bags', '')\
                .replace('bag', '').replace('contain ', '').split(' ')
            if word != '']
            for rule in f.read().strip().split('\n')]
    bagreqs2 = []
    for rule in bagreqs:
        newrule = []
        newrule.append(' '.join([rule[0], rule[1]]))
        if rule[2] == "no":
            bagreqs2.append(newrule)
            continue
        index = 2
        while index < len(rule):
            qty = int(rule[index])
            color = ' '.join([rule[index + 1], rule[index + 2]])
            for _ in range(qty):
                newrule.append(color)
            index += 3
        bagreqs2.append(newrule)
    
    bagcount = {}
    for rule in bagreqs2:
        if len(rule) == 1:
            bagcount[rule[0]] = 0
    while "shiny gold" not in bagcount.keys():
        for rule in bagreqs2:
            if rule[0] in bagcount.keys():
                continue
            if all([x in bagcount.keys() for x in rule[1:]]):
                inner = sum([bagcount[x] for x in rule[1:]])
                bagcount[rule[0]] = inner + len(rule) - 1
    return bagcount['shiny gold']
    

print(day07b())