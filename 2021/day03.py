def day03a():
	with open("2021/day03_input.txt", "r") as f:
		bits = list(zip(*f.read().strip().split("\n")))
	gamma = "0b"
	for column in bits:
		if column.count("0") * 2 > len(column):
			gamma += "0"
		else:
			gamma += "1"
	gamma = int(gamma, base=0)
	epsilon = pow(2, len(bits)) - gamma - 1
	return gamma * epsilon

def day03b():
	with open("2021/day03_input.txt", "r") as f:
		raw_bits = f.read().strip().split("\n")
	total = 1
	bit_len = len(raw_bits[0])
	for b in "01":
		bits = raw_bits[:]
		for i in range(bit_len):
			keep = list(zip(*bits))[i].count("0") * 2 > len(bits)
			bits = [num for num in bits if (num[i] != b) ^ keep]
			# Computes the exclusive or
			# Negates (num[i] != b) when True
			if len(bits) == 1:
				total *= int(bits[0], base=2)
				break
	return total


print(day03a())
print(day03b())
