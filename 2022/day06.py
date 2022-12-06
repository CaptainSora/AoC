def day06a():
	with open("2022/day06_input.txt", "r") as f:
		datastream = f.read()
	for i in range(4, len(datastream)):
		if len(set(datastream[i-3:i+1])) == 4:
			return i+1

def day06b():
	with open("2022/day06_input.txt", "r") as f:
		datastream = f.read()
	for i in range(14, len(datastream)):
		if len(set(datastream[i-13:i+1])) == 14:
			return i+1


print(day06a())
print(day06b())
