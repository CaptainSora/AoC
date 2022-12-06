def nice1(string):
	vowels = sum([string.count(v) for v in "aeiou"]) >= 3
	double = any([string[i] == string[i-1] for i in range(1, len(string))])
	banned = max([string.find(b) for b in ["ab", "cd", "pq", "xy"]]) > -1
	return vowels and double and not banned

def nice2(string):
	doubles = []
	for i in range(1, len(string)):
		doubles.append(string[i-1:i+1])
		if doubles[-1] in doubles[:-2]:
			break
	else:
		return False
	for i in range(2, len(string)):
		if string[i] == string[i-2]:
			return True
	return False


def day05a():
	with open("2015/day05_input.txt", "r") as f:
		words = f.read().strip().split("\n")
	return sum([nice1(string) for string in words])

def day05b():
	with open("2015/day05_input.txt", "r") as f:
		words = f.read().strip().split("\n")
	return sum([nice2(string) for string in words])


print(day05a())
print(day05b())
