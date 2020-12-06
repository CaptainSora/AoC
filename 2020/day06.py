def day03a():
    with open("2020/day06_input.txt", 'r') as f:
        answers = [
            group.strip().split('\n')
            for group in f.read().strip().split('\n\n')
        ]
    
    counts = 0
    for group in answers:
        questions = [0] * 26
        for person in group:
            for char in person:
                questions[ord(char) - 97] += 1
        counts += sum([x > 0 for x in questions])
    return counts

def day03b():
    with open("2020/day06_input.txt", 'r') as f:
        answers = [
            group.strip().split('\n')
            for group in f.read().strip().split('\n\n')
        ]
    
    counts = 0
    for group in answers:
        questions = [0] * 26
        for person in group:
            for char in person:
                questions[ord(char) - 97] += 1
        counts += sum([x == len(group) for x in questions])
    return counts

print(day03b())
        