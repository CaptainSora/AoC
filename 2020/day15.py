def day15a():
	instr = [int(num) for num in "8,13,1,0,18,9".split(",")]
	
	speak = instr[:]
	while len(speak) < 2020:
		last = speak[-1]
		if last not in speak[:-1]:
			speak.append(0)
		else:
			prev = 1
			while speak[-1 * prev - 1] != last:
				prev += 1
			speak.append(prev)

	return speak[-1]

# WARNING: CAN TAKE 20 SECONDS, uncomment print lines for verification
def day15b():
	instr = [int(num) for num in "8,13,1,0,18,9".split(",")]
	
	speak = {}
	counter = 1
	for i in instr[:-1]:
		speak[str(i)] = counter
		counter += 1
	last = str(instr[-1])
	while counter < 30000000:
		# if counter % 1000000 == 0:
		# 	print(counter)
		if last not in speak.keys():
			speak[last] = counter
			last = "0"
			counter += 1
		else:
			diff = counter - speak[last]
			speak[last] = counter
			last = str(diff)
			counter += 1

	return last


print(day15a())
print(day15b())
