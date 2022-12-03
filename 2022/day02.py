RPS = {"A": 0, "B": 1, "C": 2, "X": 1, "Y": 2, "Z": 3}


def rpsa(opp, action):
    """
    Returns the score of playing action against opp.
    """
    return 3 * ((RPS[action] - RPS[opp]) % 3) + RPS[action]

def rpsb(opp, result):
    """
    Returns the score of the result against opp.
    """
    return 3 * RPS[result] - 3 + (RPS[opp] + RPS[result] + 1) % 3 + 1


def day02a():
    with open("2022/day02_input.txt") as f:
        matches = [line.split(" ") for line in f.read().strip().split("\n")]
    return sum([rpsa(match[0], match[1]) for match in matches])

def day02b():
    with open("2022/day02_input.txt") as f:
        matches = [line.split(" ") for line in f.read().strip().split("\n")]
    return sum([rpsb(match[0], match[1]) for match in matches])
    

print(day02a())
print(day02b())