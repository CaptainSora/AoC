def poly(n, t):
    """
    Returns term t of the n-gonal numbers.
    Works for all n >= 1 and t >= 1.
    """
    if n < 1 or t < 1:
        return 0
    elif n == 1:
        return 1
    return int(t * ((n-2) * t - (n-4)) / 2)


def day07a():
	with open("2021/day07_input.txt", "r") as f:
		crabs = [int(num) for num in f.read().strip().split(",")]
	return min([
		sum([abs(c - pos) for c in crabs])
		for pos in range(max(crabs))
	])

def day07b():
	with open("2021/day07_input.txt", "r") as f:
		crabs = [int(num) for num in f.read().strip().split(",")]
	return min([
		sum([poly(3, abs(c - pos)) for c in crabs])
		for pos in range(max(crabs))
	])


print(day07a())
print(day07b())
