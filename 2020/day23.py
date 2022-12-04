def day23a():
	instr = [int(num) for num in "952438716"]

	def rotate(numlist, target):
		# rotates the list so that target is the 0th element.
		# modifies numlist
		while numlist[0] != target:
			numlist.append(numlist.pop(0))
		return
	
	def rotate_end(numlist, target):
		# rotates the list so that target is the last element.
		# modifies numlist
		while numlist[-1] != target:
			numlist.append(numlist.pop(0))
		return

	def pickup(numlist):
		# returns a list with actions completed
		# requires 0th item to be current cup
		# returns with 0th item as next current cup
		curcup = numlist[0]
		nextcup = curcup - 1
		pickupthree = numlist[1:4]
		remaining = [numlist[0]] + numlist[4:]
		while True:
			if nextcup == 0:
				nextcup = 9
			if nextcup in pickupthree:
				nextcup -= 1
			else:
				break
		rotate(remaining, nextcup)
		retlist = [remaining[0]] + pickupthree + remaining[1:]
		rotate_end(retlist, curcup)
		return retlist

	for _ in range(100):
		instr = pickup(instr)
	
	rotate(instr, 1)
	return ''.join([str(num) for num in instr[1:]])

# Takes about 10-15 seconds
def day23b():
	instr = [int(num) for num in "952438716"]
	linkedlist = [0] * 1000001
	for i in range(len(instr) - 1):
		linkedlist[instr[i]] = instr[i+1]
	prev = instr[-1]
	for i in range(10, 1000001):
		linkedlist[prev] = i
		prev = i
	linkedlist[1000000] = instr[0]
	# linkedlist is now a list where i is followed by j if and only if
	#   linkedlist[i] = j
	curcup = instr[0]
	for _ in range(10000000):
		three = [linkedlist[curcup]]
		for _ in range(2):
			three.append(linkedlist[three[-1]])
		# remove three, link current to after three
		linkedlist[curcup] = linkedlist[three[-1]]
		destcup = curcup - 1
		while True:
			if destcup == 0:
				destcup = 1000000
			if destcup in three:
				destcup -= 1
			else:
				break
		# link tail of three
		linkedlist[three[-1]] = linkedlist[destcup]
		# link head of three
		linkedlist[destcup] = three[0]
		# new current cup
		curcup = linkedlist[curcup]
	return linkedlist[1] * linkedlist[linkedlist[1]]


print(day23a())
print(day23b())
