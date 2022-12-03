def common(*args):
    """
    Returns the common item between all the strings.
    Assumes that there is exactly one common item.
    """
    return list(set(args[0]).intersection(*args))[0]

def wrong(string):
    """
    Returns the common letter between the two halves of the string.
    """
    return common(string[:len(string)//2], string[len(string)//2:])

def prio(item):
    """
    Returns the priority number for the item.
    """
    if item.isupper():
        return ord(item) - 64 + 26
    else:
        return ord(item) - 96


def day03a():
    with open("2022/day03_input.txt") as f:
        rucksacks = f.read().strip().split("\n")
    return sum([prio(wrong(bag)) for bag in rucksacks])

def day03b():
    with open("2022/day03_input.txt") as f:
        rucksacks = f.read().strip().split("\n")
    rucksacks = zip(rucksacks[0::3], rucksacks[1::3], rucksacks[2::3])
    return sum([prio(common(*group)) for group in rucksacks])


print(day03a())
print(day03b())