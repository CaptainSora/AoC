from math import prod


def day15a():
	with open("2015/day15_input.txt", "r") as f:
		ingr = [
			[int(num) for num in row.split()[2::2]]
			for row in f.read().strip().replace(",", "").split("\n")
		]
	max_score = 0
	for su in range(101):
		for sp in range(101-su):
			for ca in range(101-su-sp):
				ch = 100-su-sp-ca
				max_score = max(max_score, prod([
					max(0, su*ingr[0][i] + sp*ingr[1][i] + \
						ca*ingr[2][i] + ch*ingr[3][i])
					for i in range(4)
				]))
	return max_score

def day15b():
	with open("2015/day15_input.txt", "r") as f:
		ingr = [
			[int(num) for num in row.split()[2::2]]
			for row in f.read().strip().replace(",", "").split("\n")
		]
	max_score = 0
	for su in range(101):
		for sp in range(101-su):
			for ca in range(101-su-sp):
				ch = 100-su-sp-ca
				properties = [
					max(0, su*ingr[0][i] + sp*ingr[1][i] + \
						ca*ingr[2][i] + ch*ingr[3][i])
					for i in range(5)
				]
				if properties[4] == 500:
					max_score = max(max_score, prod(properties[:4]))
	return max_score


print(day15a())
print(day15b())
