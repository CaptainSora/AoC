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


def day25a():
	with open("2015/day25_input.txt", "r") as f:
		r, c = [int(num[:-1]) for num in f.read().split()[-3::2]]
	codenum = poly(3, c) + int((c + c + r - 2) * (r - 1) / 2)
	code = 20151125
	for _ in range(1, codenum):
		code = (code * 252533) % 33554393
	return code

def day25b():
	return True


print(day25a())
print(day25b())
